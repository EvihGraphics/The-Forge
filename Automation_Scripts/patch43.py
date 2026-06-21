import sys

file_path = 'Examples_3/Unit_Tests/src/15_Transparency/15_Transparency.cpp'
with open(file_path, 'rb') as f:
    content = f.read()

if content.startswith(b'\xef\xbf\xbd?*'):
    content = b'/*' + content[4:]

# Wait, the first character output was "?*", which could be a corrupted BOM. 
# Let's just strip everything up to the first "*" and put "/*"
import re
content_str = content.decode('utf-8', errors='ignore')
content_str = re.sub(r'^.*?(\n \* Copyright)', r'/*\1', content_str, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content_str)

print("Patch 43 applied.")
