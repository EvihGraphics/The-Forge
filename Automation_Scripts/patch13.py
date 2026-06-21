content = '''#ifndef AVBOIT_H_FSL
#define AVBOIT_H_FSL

#define AVBOIT_VOLUME_WIDTH 1920
#define AVBOIT_VOLUME_HEIGHT 1080
#define AVBOIT_VOLUME_DEPTH 64

#ifdef AVBOIT_UNORDERED_ACCESS
RES(RWTex3D(uint), VolumeExtinctionBufferUAV, UPDATE_FREQ_PER_FRAME, u1, binding = 5);
RES(RWTex3D(float4), VolumeTransmittanceLutUAV, UPDATE_FREQ_PER_FRAME, u2, binding = 6);
RES(RWTex3D(uint), VolumeColorBufferUAV, UPDATE_FREQ_PER_FRAME, u3, binding = 7);
#endif

#ifdef AVBOIT_ORDERED_ACCESS
RES(Tex3D(uint), VolumeExtinctionBufferSRV, UPDATE_FREQ_NONE, t1, binding = 5);
RES(Tex3D(float4), VolumeTransmittanceLutSRV, UPDATE_FREQ_NONE, t2, binding = 6);
RES(Tex3D(uint), VolumeColorBufferSRV, UPDATE_FREQ_NONE, t3, binding = 7);
#endif

CBUFFER(AVBOITUniforms, UPDATE_FREQ_PER_FRAME, b2, binding = 7)
{
    DATA(uint, volumeWidth, None);
    DATA(uint, volumeHeight, None);
    DATA(uint, volumeDepth, None);
    DATA(float, pad, None);
};

uint PackExtinction(float3 ext)
{
    const float maxExt = 3.0f;
    uint3 packed = uint3(clamp(ext / maxExt, 0.0f, 1.0f) * 255.0f);
    return packed.x | (packed.y << 8) | (packed.z << 16);
}

float3 UnpackExtinction(uint packed)
{
    const float maxExt = 3.0f;
    float3 ext;
    ext.x = (packed & 0xFF) / 255.0f;
    ext.y = ((packed >> 8) & 0xFF) / 255.0f;
    ext.z = ((packed >> 16) & 0xFF) / 255.0f;
    return ext * maxExt;
}

#endif
'''
with open('Examples_3/Unit_Tests/src/15_Transparency/Shaders/FSL/avboit.h.fsl', 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 13 applied.")
