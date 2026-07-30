import os
import re

# Sökvägen till dina blogginlägg
content_dir = 'content/blogg'

if not os.path.exists(content_dir):
    print(f"Fel: Hittade inte mappen '{content_dir}'")
    exit(1)

count = 0
for root, dirs, files in os.walk(content_dir):
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Ersätter categories: med kategorier: i början av en rad
            new_content = re.sub(r'^categories\s*:', 'kategorier:', content, flags=re.MULTILINE)
            
            if new_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1

print(f"Klart! Uppdaterade {count} blogginlägg.")
