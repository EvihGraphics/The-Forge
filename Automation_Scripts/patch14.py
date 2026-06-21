import sys

file_path = 'Examples_3/Unit_Tests/src/15_Transparency/Shaders/FSL/AVBOIT.frag.fsl'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('AtomicAdd(Get(VolumeExtinctionBufferUAV)[coords], packedExt);', 'uint dummy;\n    AtomicAdd(Get(VolumeExtinctionBufferUAV)[coords], packedExt, dummy);')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 14 applied.")
