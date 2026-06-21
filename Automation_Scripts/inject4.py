import re
import sys

file_path = 'Examples_3/Unit_Tests/src/15_Transparency/15_Transparency.cpp'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

def inject(pattern, new_code):
    global content
    matches = list(re.finditer(pattern, content, re.MULTILINE))
    if not matches:
        print(f"Failed to find pattern: {pattern}")
        sys.exit(1)
    match = matches[-1]
    content = content[:match.end()] + "\n" + new_code + content[match.end():]
    print(f"Injected successfully after {pattern.strip()[:30]}")

inject(r'addResource\(&aoitClearMaskTextureLoadDesc, NULL\);', '''
            TextureDesc avboitExtinctionDesc = {};
            avboitExtinctionDesc.mArraySize = 1;
            avboitExtinctionDesc.mDepth = 64; // volumeDepth
            avboitExtinctionDesc.mDescriptors = DESCRIPTOR_TYPE_TEXTURE | DESCRIPTOR_TYPE_RW_TEXTURE;
            avboitExtinctionDesc.mFormat = TinyImageFormat_R32_UINT;
            avboitExtinctionDesc.mHeight = 1080;
            avboitExtinctionDesc.mMipLevels = 1;
            avboitExtinctionDesc.mSampleCount = SAMPLE_COUNT_1;
            avboitExtinctionDesc.mStartState = RESOURCE_STATE_UNORDERED_ACCESS;
            avboitExtinctionDesc.mWidth = 1920;
            avboitExtinctionDesc.pName = "AVBOITVolumeExtinction";
            TextureLoadDesc avboitExtinctionLoadDesc = {};
            avboitExtinctionLoadDesc.pDesc = &avboitExtinctionDesc;
            avboitExtinctionLoadDesc.ppTexture = &pTextureAVBOITVolumeExtinction;
            addResource(&avboitExtinctionLoadDesc, NULL);

            TextureDesc avboitTransmittanceDesc = {};
            avboitTransmittanceDesc.mArraySize = 1;
            avboitTransmittanceDesc.mDepth = 64;
            avboitTransmittanceDesc.mDescriptors = DESCRIPTOR_TYPE_TEXTURE | DESCRIPTOR_TYPE_RW_TEXTURE;
            avboitTransmittanceDesc.mFormat = TinyImageFormat_R16G16B16A16_SFLOAT;
            avboitTransmittanceDesc.mHeight = 1080;
            avboitTransmittanceDesc.mMipLevels = 1;
            avboitTransmittanceDesc.mSampleCount = SAMPLE_COUNT_1;
            avboitTransmittanceDesc.mStartState = RESOURCE_STATE_UNORDERED_ACCESS;
            avboitTransmittanceDesc.mWidth = 1920;
            avboitTransmittanceDesc.pName = "AVBOITVolumeTransmittanceLut";
            TextureLoadDesc avboitTransmittanceLoadDesc = {};
            avboitTransmittanceLoadDesc.pDesc = &avboitTransmittanceDesc;
            avboitTransmittanceLoadDesc.ppTexture = &pTextureAVBOITVolumeTransmittanceLut;
            addResource(&avboitTransmittanceLoadDesc, NULL);

            BufferLoadDesc avboitUniformDesc = {};
            avboitUniformDesc.mDesc.mDescriptors = DESCRIPTOR_TYPE_UNIFORM_BUFFER;
            avboitUniformDesc.mDesc.mMemoryUsage = RESOURCE_MEMORY_USAGE_CPU_TO_GPU;
            avboitUniformDesc.mDesc.mSize = sizeof(uint32_t) * 4;
            avboitUniformDesc.mDesc.mFlags = BUFFER_CREATION_FLAG_PERSISTENT_MAP_BIT;
            avboitUniformDesc.pData = NULL;
            for (uint32_t i = 0; i < gDataBufferCount; ++i)
            {
                avboitUniformDesc.ppBuffer = &pBufferAVBOITUniform[i];
                addResource(&avboitUniformDesc, NULL);
            }
''')

inject(r'removeResource\(pTextureAOITClearMask\);', '''
            removeResource(pTextureAVBOITVolumeExtinction);
            removeResource(pTextureAVBOITVolumeTransmittanceLut);
            for (uint32_t i = 0; i < gDataBufferCount; ++i)
                removeResource(pBufferAVBOITUniform[i]);
''')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Injection Phase 3 complete.")
