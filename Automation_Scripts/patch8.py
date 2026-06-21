import sys

file_path = 'Examples_3/Unit_Tests/src/15_Transparency/Shaders/FSL/ShaderList.fsl'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace incorrect lines
content = content.replace('#frag AVBOIT.frag', '#frag AVBOIT.frag\n#include "AVBOIT.frag.fsl"\n#end\n')
content = content.replace('#comp avboit_clear.comp', '#comp avboit_clear.comp\n#include "avboit_clear.comp.fsl"\n#end\n')
content = content.replace('#comp avboit_integrate.comp', '#comp avboit_integrate.comp\n#include "avboit_integrate.comp.fsl"\n#end\n')
content = content.replace('#frag avboit_composite.frag', '#frag avboit_composite.frag\n#include "avboit_composite.frag.fsl"\n#end\n')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 8 applied.")
