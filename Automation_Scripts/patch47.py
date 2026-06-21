import sys

file_path = 'Examples_3/Unit_Tests/src/15_Transparency/Shaders/FSL/ShaderList.fsl'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

if 'avboit_forward.frag' not in content:
    content += '\n#frag avboit_forward.frag\n#include "avboit_forward.frag.fsl"\n#end\n'

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 47 applied.")
