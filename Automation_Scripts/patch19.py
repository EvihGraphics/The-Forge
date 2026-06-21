import sys

file_path = 'Examples_3/Unit_Tests/src/15_Transparency/Shaders/FSL/avboit.h.fsl'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix GetVolumeIndex placement
content = content.replace('#endif\n\nuint GetVolumeIndex(uint3 coords)\n{\n    return coords.z * AVBOIT_VOLUME_WIDTH * AVBOIT_VOLUME_HEIGHT + coords.y * AVBOIT_VOLUME_WIDTH + coords.x;\n}\n', '')

# Insert it before #endif
content = content.replace('#endif', '''
uint GetVolumeIndex(uint3 coords)
{
    return coords.z * AVBOIT_VOLUME_WIDTH * AVBOIT_VOLUME_HEIGHT + coords.y * AVBOIT_VOLUME_WIDTH + coords.x;
}

#endif''')

# Change RWTex3D to WTex3D for Lut
content = content.replace('RWTex3D(float4), VolumeTransmittanceLutUAV', 'WTex3D(float4), VolumeTransmittanceLutUAV')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 19 applied.")
