import sys

file_path = 'Examples_3/Unit_Tests/src/15_Transparency/Shaders/FSL/avboit.h.fsl'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('(float)(packed & 0xFF)', 'float(packed & 0xFF)')
content = content.replace('(float)((packed >> 8) & 0xFF)', 'float((packed >> 8) & 0xFF)')
content = content.replace('(float)((packed >> 16) & 0xFF)', 'float((packed >> 16) & 0xFF)')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 21 applied.")
