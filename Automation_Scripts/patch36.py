import sys

file_path = 'Examples_3/Unit_Tests/src/15_Transparency/Shaders/FSL/avboit.h.fsl'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('CBUFFER(AVBOITUniforms, UPDATE_FREQ_PER_FRAME, b2, binding = 7)', 'CBUFFER(AVBOITUniforms, UPDATE_FREQ_PER_FRAME, b5, binding = 10)')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 36 applied.")
