import sys

file_path = 'Examples_3/Unit_Tests/src/15_Transparency/Shaders/FSL/avboit_composite.frag.fsl'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the dummy output with the actual transmittance output
content = content.replace('float4 outColor = float4(1.0f - totalTransmittance, 1.0f); // Dummy color to test baseline', 'float4 outColor = float4(totalTransmittance, 1.0f);')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 45 applied.")
