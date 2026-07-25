import os
import sys
import glob
import re
from openai import OpenAI

def generate_ai_description(client, content):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Du är en assistent som skriver korta, engagerande sammanfattningar för blogginlägg. Texten MÅSTE vara på svenska och max 150 tecken inklusive mellanslag. Gå rakt på sak utan inledningar som 'Det här inlägget handlar om'."},
                {"role": "user", "content": f"Sammanfatta följande text:\n\n{content[:2000]}"}
            ],
            max_tokens=60,
            temperature=0.5
        )
        raw_desc = response.choices[0].message.content.strip()
        
        # FRAMTIDSSÄKRING 1: Ersätt automatiskt alla inre dubbelcitat med enkla apostrofer
        # Om AI:n svarar: Text "Titel" text -> Blir det: Text 'Titel' text
        if raw_desc.startswith('"') and raw_desc.endswith('"'):
            inner_text = raw_desc[1:-1]
            cleaned_inner = inner_text.replace('"', "'")
            return cleaned_inner
        else:
            return raw_desc.replace('"', "'")
            
    except Exception as e:
        print(f"  [API-FEL] Kunde inte generera AI-text: {e}")
        return None

def process_file(file_path, client):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    if not lines or lines[0].strip() != '---':
        return False

    end_fm_idx = -1
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            end_fm_idx = i
            break

    if end_fm_idx == -1:
        return False

    front_matter_lines = lines[1:end_fm_idx]
    body_lines = lines[end_fm_idx+1:]

    has_description = False
    has_images = False
    post_title = "Blogginlägg"
    
    for line in front_matter_lines:
        clean_line = line.strip()
        if clean_line.startswith('description:') or clean_line.startswith('description :'):
            has_description = True
        if clean_line.startswith('images:') or clean_line.startswith('images :'):
            has_images = True
        if clean_line.startswith('title:') or clean_line.startswith('title :'):
            title_match = re.search(r'title\s*:\s*"(.*?)"', clean_line)
            if title_match:
                post_title = title_match.group(1)

    if has_description and has_images:
        return False

    body_text = "".join(body_lines).strip()
    clean_body = re.sub(r'<!--.*?-->', '', body_text, flags=re.DOTALL).strip()
    
    img_match = re.search(r'!\[.*?\]\((.*?)\)', clean_body)
    yt_match = re.search(r'\{\{<\s*youtube-enhanced\s+([a-zA-Z0-9_-]+)', clean_body)

    found_image_url = None
    if img_match:
        raw_url = img_match.group(1).strip()
        # FRAMTIDSSÄKRING 2: Om du skrivit en bildtext, t.ex. /images/bild.jpg "Text", 
        # klipper vi bort texten direkt så bara bildlänken sparas på image-raden.
        url_clean_match = re.search(r'^([^\s"\']+\.(jpg|png|jpeg|gif|svg|webp))', raw_url)
        if url_clean_match:
            found_image_url = url_clean_match.group(1)
        else:
            found_image_url = raw_url.split()[0].strip('"').strip("'")
    elif yt_match:
        yt_id = yt_match.group(1)
        found_image_url = f"https://youtube.com{yt_id}/maxresdefault.jpg"

    ai_reading_text = re.sub(r'\{\{<.*?>\}\}', '', clean_body).strip()
    word_count = len(ai_reading_text.split())

    added_lines = []
    if not has_description:
        if word_count > 10:
            ai_desc = generate_ai_description(client, ai_reading_text)
        else:
            ai_desc = f"Se videoklippet tillhörande inlägget '{post_title}' på Joakim Frögrens blogg."
            if len(ai_desc) > 150:
                ai_desc = f"Videoklipp: {post_title}."
        
        if ai_desc:
            added_lines.append(f'description: "{ai_desc}"\n')

    if found_image_url and not has_images:
        added_lines.append(f'images:\n  - "{found_image_url}"\n')

    if not added_lines:
        return False

    print(f"Uppdaterar metadata för: {file_path}")
    new_lines = lines[:end_fm_idx] + added_lines + lines[end_fm_idx:]

    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    return True

def main():
    if not os.environ.get("OPENAI_API_KEY"):
        print("Fel: Miljövariabeln OPENAI_API_KEY saknas.")
        sys.exit(1)

    client = OpenAI()
    content_path = os.path.join(".", "content", "**", "*.md")
    files = glob.glob(content_path, recursive=True)
    
    updated_count = 0
    for file_path in files:
        try:
            if process_file(file_path, client):
                updated_count += 1
        except Exception as e:
            print(f"Fel vid hantering av {file_path}: {e}")

    if updated_count > 0:
        print(f"\nKlart! {updated_count} nya inlägg har framtidssäkrats.")

if __name__ == "__main__":
    main()

