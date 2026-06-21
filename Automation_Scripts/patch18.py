import sys

# Update avboit_clear.comp.fsl
clear_path = 'Examples_3/Unit_Tests/src/15_Transparency/Shaders/FSL/avboit_clear.comp.fsl'
with open(clear_path, 'r', encoding='utf-8') as f:
    clear_content = f.read()

clear_content = clear_content.replace('void CS_MAIN( SV_DispatchThreadID(uint3) DTid )', 'void CS_MAIN( SV_DispatchThreadID(uint3) DTid )\n{\n    INIT_MAIN;\n')
clear_content = clear_content.replace('{\n{\n', '{\n')
clear_content = clear_content.replace('Write3D(Get(VolumeExtinctionBufferUAV), DTid, 0);', 'Get(VolumeExtinctionBufferUAV)[GetVolumeIndex(DTid)] = 0;')
clear_content = clear_content.replace('Write3D(Get(VolumeColorBufferUAV), DTid, 0);', 'Get(VolumeColorBufferUAV)[GetVolumeIndex(DTid)] = 0;')

with open(clear_path, 'w', encoding='utf-8') as f:
    f.write(clear_content)

# Update avboit_integrate.comp.fsl
int_path = 'Examples_3/Unit_Tests/src/15_Transparency/Shaders/FSL/avboit_integrate.comp.fsl'
with open(int_path, 'r', encoding='utf-8') as f:
    int_content = f.read()

int_content = int_content.replace('void CS_MAIN( SV_DispatchThreadID(uint3) DTid )', 'void CS_MAIN( SV_DispatchThreadID(uint3) DTid )\n{\n    INIT_MAIN;\n')
int_content = int_content.replace('{\n{\n', '{\n')
int_content = int_content.replace('uint packedExt = LoadTex3D(Get(VolumeExtinctionBufferSRV), NO_SAMPLER, coords, 0).r;', 'uint packedExt = Get(VolumeExtinctionBufferSRV)[GetVolumeIndex(coords)];')

with open(int_path, 'w', encoding='utf-8') as f:
    f.write(int_content)

print("Patch 18 applied.")
