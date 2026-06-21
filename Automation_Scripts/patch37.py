import sys
import re

file_path = 'Examples_3/Unit_Tests/src/15_Transparency/Shaders/FSL/AVBOIT.frag.fsl'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the manual VSOutput struct
pattern = r'STRUCT\(VSOutput\)\s*\{[^\}]*\};\s*'
content = re.sub(pattern, '#include "shaderDefs.h.fsl"\n\n', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 37 applied.")
