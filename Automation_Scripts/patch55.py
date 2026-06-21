import sys

file_path = 'Examples_3/Unit_Tests/src/15_Transparency/Shaders/FSL/avboit_forward.frag.fsl'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

old_code = '''    uint3 coords = uint3(pixelAddr.x, pixelAddr.y, zIndex);
    
    // Sample Transmittance from LUT
    float4 lutValue = LoadTex3D(Get(VolumeTransmittanceLutSRV), NO_SAMPLER, coords, 0);
    float3 transmittanceFront = lutValue.rgb;'''

new_code = '''    // Sample Transmittance from LUT at previous depth slice
    float3 transmittanceFront = float3(1.0f, 1.0f, 1.0f);
    if(zIndex > 0)
    {
        uint3 prevCoords = uint3(pixelAddr.x, pixelAddr.y, zIndex - 1);
        float4 lutValue = LoadTex3D(Get(VolumeTransmittanceLutSRV), NO_SAMPLER, prevCoords, 0);
        transmittanceFront = lutValue.rgb;
    }'''

content = content.replace(old_code, new_code)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 55 applied.")
