import sys
import re

file_path = 'Examples_3/Unit_Tests/src/15_Transparency/15_Transparency.cpp'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix clearBarriers
content = content.replace('''    TextureBarrier clearBarriers[] = {
        { pBufferAVBOITVolumeExtinction, RESOURCE_STATE_PIXEL_SHADER_RESOURCE, RESOURCE_STATE_UNORDERED_ACCESS },
        { pTextureAVBOITVolumeTransmittanceLut, RESOURCE_STATE_PIXEL_SHADER_RESOURCE, RESOURCE_STATE_UNORDERED_ACCESS }
    };
    cmdResourceBarrier(pCmd, 0, NULL, 2, clearBarriers, 0, NULL);''',
'''    BufferBarrier clearBufBarriers[] = {
        { pBufferAVBOITVolumeExtinction, RESOURCE_STATE_PIXEL_SHADER_RESOURCE, RESOURCE_STATE_UNORDERED_ACCESS }
    };
    TextureBarrier clearTexBarriers[] = {
        { pTextureAVBOITVolumeTransmittanceLut, RESOURCE_STATE_PIXEL_SHADER_RESOURCE, RESOURCE_STATE_UNORDERED_ACCESS }
    };
    cmdResourceBarrier(pCmd, 1, clearBufBarriers, 1, clearTexBarriers, 0, NULL);''')

# Fix splatBarriers
content = content.replace('''    TextureBarrier splatBarriers[] = {
        { pBufferAVBOITVolumeExtinction, RESOURCE_STATE_UNORDERED_ACCESS, RESOURCE_STATE_UNORDERED_ACCESS }
    };
    cmdResourceBarrier(pCmd, 0, NULL, 1, splatBarriers, 0, NULL);''',
'''    BufferBarrier splatBarriers[] = {
        { pBufferAVBOITVolumeExtinction, RESOURCE_STATE_UNORDERED_ACCESS, RESOURCE_STATE_UNORDERED_ACCESS }
    };
    cmdResourceBarrier(pCmd, 1, splatBarriers, 0, NULL, 0, NULL);''')

# Fix integrateBarriers
content = content.replace('''    TextureBarrier integrateBarriers[] = {
        { pBufferAVBOITVolumeExtinction, RESOURCE_STATE_UNORDERED_ACCESS, RESOURCE_STATE_PIXEL_SHADER_RESOURCE }
    };
    cmdResourceBarrier(pCmd, 0, NULL, 1, integrateBarriers, 0, NULL);''',
'''    BufferBarrier integrateBarriers[] = {
        { pBufferAVBOITVolumeExtinction, RESOURCE_STATE_UNORDERED_ACCESS, RESOURCE_STATE_PIXEL_SHADER_RESOURCE }
    };
    cmdResourceBarrier(pCmd, 1, integrateBarriers, 0, NULL, 0, NULL);''')

# Fix allocation (Load)
content = re.sub(
    r'TextureDesc\s+avboitExtinctionDesc\s*=\s*\{\};.*avboitExtinctionLoadDesc\.ppBuffer\s*=\s*&pBufferAVBOITVolumeExtinction;\s*addResource\(&avboitExtinctionLoadDesc,\s*NULL\);',
    r'''BufferLoadDesc avboitExtLoadDesc = {};
            avboitExtLoadDesc.mDesc.mDescriptors = DESCRIPTOR_TYPE_RW_BUFFER | DESCRIPTOR_TYPE_BUFFER;
            avboitExtLoadDesc.mDesc.mMemoryUsage = RESOURCE_MEMORY_USAGE_GPU_ONLY;
            avboitExtLoadDesc.mDesc.mElementCount = 1920 * 1080 * 64;
            avboitExtLoadDesc.mDesc.mStructStride = sizeof(uint32_t);
            avboitExtLoadDesc.mDesc.mSize = avboitExtLoadDesc.mDesc.mElementCount * avboitExtLoadDesc.mDesc.mStructStride;
            avboitExtLoadDesc.mDesc.mStartState = RESOURCE_STATE_PIXEL_SHADER_RESOURCE;
            avboitExtLoadDesc.mDesc.pName = "AVBOITVolumeExtinction";
            avboitExtLoadDesc.ppBuffer = &pBufferAVBOITVolumeExtinction;
            addResource(&avboitExtLoadDesc, NULL);''',
    content, flags=re.DOTALL
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 24 applied.")
