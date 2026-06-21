import sys

# Update avboit.h.fsl
file_path = 'Examples_3/Unit_Tests/src/15_Transparency/Shaders/FSL/avboit.h.fsl'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('RES(RWTex3D(uint), VolumeExtinctionBufferUAV, UPDATE_FREQ_PER_FRAME, u1, binding = 5);', 'RES(RWBuffer(uint), VolumeExtinctionBufferUAV, UPDATE_FREQ_PER_FRAME, u1, binding = 5);')
content = content.replace('RES(RWTex3D(uint), VolumeColorBufferUAV, UPDATE_FREQ_PER_FRAME, u3, binding = 7);', 'RES(RWBuffer(uint), VolumeColorBufferUAV, UPDATE_FREQ_PER_FRAME, u3, binding = 7);')

content = content.replace('RES(Tex3D(uint), VolumeExtinctionBufferSRV, UPDATE_FREQ_NONE, t1, binding = 5);', 'RES(Buffer(uint), VolumeExtinctionBufferSRV, UPDATE_FREQ_NONE, t1, binding = 5);')
content = content.replace('RES(Tex3D(uint), VolumeColorBufferSRV, UPDATE_FREQ_NONE, t3, binding = 7);', 'RES(Buffer(uint), VolumeColorBufferSRV, UPDATE_FREQ_NONE, t3, binding = 7);')

# Add utility for flattening index
content += '''
uint GetVolumeIndex(uint3 coords)
{
    return coords.z * AVBOIT_VOLUME_WIDTH * AVBOIT_VOLUME_HEIGHT + coords.y * AVBOIT_VOLUME_WIDTH + coords.x;
}
'''

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

# Update AVBOIT.frag.fsl
frag_path = 'Examples_3/Unit_Tests/src/15_Transparency/Shaders/FSL/AVBOIT.frag.fsl'
with open(frag_path, 'r', encoding='utf-8') as f:
    frag_content = f.read()

frag_content = frag_content.replace('uint dummy;\\n    AtomicAdd(Get(VolumeExtinctionBufferUAV)[coords], packedExt, dummy);', 'uint dummy;\n    AtomicAdd(Get(VolumeExtinctionBufferUAV)[GetVolumeIndex(coords)], packedExt, dummy);')

with open(frag_path, 'w', encoding='utf-8') as f:
    f.write(frag_content)

# Update avboit_clear.comp.fsl
clear_path = 'Examples_3/Unit_Tests/src/15_Transparency/Shaders/FSL/avboit_clear.comp.fsl'
with open(clear_path, 'r', encoding='utf-8') as f:
    clear_content = f.read()

clear_content = clear_content.replace('Write3D(Get(VolumeExtinctionBufferUAV), coords, 0);', 'Get(VolumeExtinctionBufferUAV)[GetVolumeIndex(coords)] = 0;')
clear_content = clear_content.replace('Write3D(Get(VolumeColorBufferUAV), coords, 0);', 'Get(VolumeColorBufferUAV)[GetVolumeIndex(coords)] = 0;')

with open(clear_path, 'w', encoding='utf-8') as f:
    f.write(clear_content)

# Update avboit_integrate.comp.fsl
int_path = 'Examples_3/Unit_Tests/src/15_Transparency/Shaders/FSL/avboit_integrate.comp.fsl'
with open(int_path, 'r', encoding='utf-8') as f:
    int_content = f.read()

int_content = int_content.replace('uint packedExt = LoadRWTex3D(Get(VolumeExtinctionBufferUAV), coords).r;', 'uint packedExt = Get(VolumeExtinctionBufferUAV)[GetVolumeIndex(coords)];')

with open(int_path, 'w', encoding='utf-8') as f:
    f.write(int_content)

print("Patch 16 applied.")
