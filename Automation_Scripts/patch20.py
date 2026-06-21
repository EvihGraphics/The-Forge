import sys

file_path = 'Examples_3/Unit_Tests/src/15_Transparency/Shaders/FSL/avboit.h.fsl'
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Remove lines 1, 2 and 50
new_lines = []
for i, line in enumerate(lines):
    if i == 0 and '#ifndef' in line: continue
    if i == 1 and '#define' in line: continue
    if i == 49 and '#endif' in line: continue
    new_lines.append(line)

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Patch 20 applied.")
