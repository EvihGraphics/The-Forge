import re

file_path = 'Examples_3/Unit_Tests/src/15_Transparency/15_Transparency.cpp'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace { "...", NULL, 0 } with { "..." }
content = re.sub(r'\{\s*"([^"]+)",\s*NULL,\s*0\s*\}', r'{ "\1" }', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 6 applied.")
