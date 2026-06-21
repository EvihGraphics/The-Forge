import sys

frag_path = 'Examples_3/Unit_Tests/src/15_Transparency/Shaders/FSL/AVBOIT.frag.fsl'
with open(frag_path, 'r', encoding='utf-8') as f:
    frag_content = f.read()

frag_content = frag_content.replace(
    'uint dummy;\n    AtomicAdd(Get(VolumeExtinctionBufferUAV)[GetVolumeIndex(coords)], packedExt, dummy);',
    'uint dummy;\n    uint flatIdx = GetVolumeIndex(coords);\n    AtomicAdd(Get(VolumeExtinctionBufferUAV)[flatIdx], packedExt, dummy);'
)

with open(frag_path, 'w', encoding='utf-8') as f:
    f.write(frag_content)

print("Patch 17 applied.")
