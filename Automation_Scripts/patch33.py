import sys

file_path = 'Examples_3/Unit_Tests/src/15_Transparency/Shaders/FSL/AVBOIT.frag.fsl'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('float4 PS_MAIN( VSOutput In )', 'void PS_MAIN( VSOutput In )')
content = content.replace('    clip(-1.0f);\n    RETURN(float4(0,0,0,0));', '    RETURN();')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 33 applied.")
