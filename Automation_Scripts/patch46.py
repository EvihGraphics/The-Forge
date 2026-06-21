import sys

file_path = 'Examples_3/Unit_Tests/src/15_Transparency/Shaders/FSL/avboit_forward.frag.fsl'
content = '''#include "shaderDefs.h.fsl"
#define AVBOIT_ORDERED_ACCESS
#include "avboit.h.fsl"
#include "shading.h.fsl"

STRUCT(VSOutput)
{
    DATA(float4, Position, SV_Position);
    DATA(float4, WorldPosition, POSITION);
    DATA(float4, Normal, NORMAL);
    DATA(float4, UV, TEXCOORD0);
    DATA(FLAT(uint), MatID, MAT_ID);
#if FT_MULTIVIEW
    DATA(FLAT(uint), ViewID, TEXCOORD1);
#endif
};

EARLY_FRAGMENT_TESTS
float4 PS_MAIN( VSOutput In )
{
    INIT_MAIN;
    float4 baseColor = Shade(In.MatID, In.UV.xy, In.WorldPosition.xyz, normalize(In.Normal.xyz), VR_VIEW_ID(In.ViewID));
    
    if (baseColor.a <= 0.01f)
    {
        clip(-1.0f);
        RETURN(float4(0, 0, 0, 0));
    }
    
    uint2 pixelAddr = uint2(In.Position.xy);
    float depth = In.Position.z;
    uint zIndex = clamp(uint(depth * volumeDepth), 0, volumeDepth - 1);
    
    uint3 coords = uint3(pixelAddr.x, pixelAddr.y, zIndex);
    
    // Sample Transmittance from LUT
    float4 lutValue = LoadTex3D(Get(VolumeTransmittanceLutSRV), NO_SAMPLER, coords, 0);
    float3 transmittanceFront = lutValue.rgb;
    
    // finalColor = baseColor.rgb * transmittanceFront * baseColor.a
    float3 finalLuminance = baseColor.rgb * transmittanceFront * baseColor.a;
    
    RETURN(float4(finalLuminance, 1.0f));
}
'''

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 46 applied.")
