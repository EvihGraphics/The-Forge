import sys

file_path = 'Examples_3/Unit_Tests/src/15_Transparency/Shaders/FSL/AVBOIT.frag.fsl'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('AtomicAdd3D(Get(VolumeExtinctionBufferUAV), coords, packedExt);', 'AtomicAdd(Get(VolumeExtinctionBufferUAV)[coords], packedExt);')
content = content.replace('Out.Color = float4(0.0f, 0.0f, 0.0f, 0.0f);', 'float4 OutColor = float4(0.0f, 0.0f, 0.0f, 0.0f);')
content = content.replace('RETURN(Out);', 'RETURN(OutColor);')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 9 applied.")
