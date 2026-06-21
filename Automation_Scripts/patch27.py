import sys

file_path = 'Examples_3/Unit_Tests/src/15_Transparency/Shaders/FSL/AVBOIT.frag.fsl'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('float4 PS_MAIN', 'void PS_MAIN')
content = content.replace('    float4 OutColor = float4(0.0f, 0.0f, 0.0f, 0.0f);\n    RETURN(OutColor);', '    RETURN();')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 27 applied.")
