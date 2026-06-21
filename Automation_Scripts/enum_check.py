import re
with open(r'D:\Users\l3d\Documents\AVBOIT\The-Forge\Examples_3\Unit_Tests\src\15_Transparency\15_Transparency.cpp', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'typedef enum TransparencyType\s*\{([^}]+)\}', content)
if match:
    lines = match.group(1).split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if line:
            print(f"{line}")
