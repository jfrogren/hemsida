import os
import re

# Sökvägen till dina blogginlägg
content_dir = 'content/blogg'

if not os.path.exists(content_dir):
    print(f"Fel: Hittade inte mappen '{content_dir}'")
    exit(1)

updated_count = 0
skipped_count = 0

for root, dirs, files in os.walk(content_dir):
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Kontrollera om inlägget redan har en slug
            if 'slug:' in content:
                skipped_count += 1
                continue
            
            # Ta bort filändelsen .md
            filename_base = file.rsplit('.', 1)[0]
            
            # Ta bort det inledande datumet (t.ex. 2026-07-19-)
            slug_value = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', filename_base)
            
            # Skapa den nya slug-raden
            slug_line = f'slug: "{slug_value}"'
            
            # Skjut in slug-raden direkt under den allra första --- raden
            new_content = content.replace('---', f'---\n{slug_line}', 1)
            
            # Spara filen med det nya innehållet
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
                
            updated_count += 1

print(f"Klart! {updated_count} inlägg uppdaterades med en ny slug.")
print(f"{skipped_count} inlägg hoppades över eftersom de redan hade en slug.")
