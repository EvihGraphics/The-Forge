import sys

cpp_path = 'Examples_3/Unit_Tests/src/15_Transparency/15_Transparency.cpp'
with open(cpp_path, 'r', encoding='utf-8') as f:
    cpp_content = f.read()

# Replace Extinction TextureDesc with BufferLoadDesc
cpp_content = cpp_content.replace('''    TextureDesc avboitExtDesc = {};
    avboitExtDesc.mArraySize = 1;
    avboitExtDesc.mDepth = AVBOIT_VOLUME_DEPTH;
    avboitExtDesc.mWidth = mSettings.mWidth;
    avboitExtDesc.mHeight = mSettings.mHeight;
    avboitExtDesc.mMipLevels = 1;
    avboitExtDesc.mSampleCount = SAMPLE_COUNT_1;
    avboitExtDesc.mFormat = TinyImageFormat_R32_UINT;
    avboitExtDesc.mStartState = RESOURCE_STATE_PIXEL_SHADER_RESOURCE;
    avboitExtDesc.mDescriptors = DESCRIPTOR_TYPE_TEXTURE | DESCRIPTOR_TYPE_RW_TEXTURE;
    avboitExtDesc.pName = "AVBOIT Volume Extinction";
    addTexture(pRenderer, &avboitExtDesc, &pTextureAVBOITVolumeExtinction);''',
'''    BufferLoadDesc avboitExtDesc = {};
    avboitExtDesc.mDesc.mDescriptors = DESCRIPTOR_TYPE_RW_BUFFER | DESCRIPTOR_TYPE_BUFFER;
    avboitExtDesc.mDesc.mMemoryUsage = RESOURCE_MEMORY_USAGE_GPU_ONLY;
    avboitExtDesc.mDesc.mElementCount = mSettings.mWidth * mSettings.mHeight * AVBOIT_VOLUME_DEPTH;
    avboitExtDesc.mDesc.mStructStride = sizeof(uint32_t);
    avboitExtDesc.mDesc.mSize = avboitExtDesc.mDesc.mElementCount * avboitExtDesc.mDesc.mStructStride;
    avboitExtDesc.pData = NULL;
    avboitExtDesc.ppBuffer = &pBufferAVBOITVolumeExtinction;
    addResource(&avboitExtDesc, NULL);''')

# Replace Color TextureDesc with BufferLoadDesc
cpp_content = cpp_content.replace('''    TextureDesc avboitColorDesc = {};
    avboitColorDesc.mArraySize = 1;
    avboitColorDesc.mDepth = AVBOIT_VOLUME_DEPTH;
    avboitColorDesc.mWidth = mSettings.mWidth;
    avboitColorDesc.mHeight = mSettings.mHeight;
    avboitColorDesc.mMipLevels = 1;
    avboitColorDesc.mSampleCount = SAMPLE_COUNT_1;
    avboitColorDesc.mFormat = TinyImageFormat_R32_UINT;
    avboitColorDesc.mStartState = RESOURCE_STATE_PIXEL_SHADER_RESOURCE;
    avboitColorDesc.mDescriptors = DESCRIPTOR_TYPE_TEXTURE | DESCRIPTOR_TYPE_RW_TEXTURE;
    avboitColorDesc.pName = "AVBOIT Volume Color";
    addTexture(pRenderer, &avboitColorDesc, &pTextureAVBOITVolumeColor);''',
'''    BufferLoadDesc avboitColorDesc = {};
    avboitColorDesc.mDesc.mDescriptors = DESCRIPTOR_TYPE_RW_BUFFER | DESCRIPTOR_TYPE_BUFFER;
    avboitColorDesc.mDesc.mMemoryUsage = RESOURCE_MEMORY_USAGE_GPU_ONLY;
    avboitColorDesc.mDesc.mElementCount = mSettings.mWidth * mSettings.mHeight * AVBOIT_VOLUME_DEPTH;
    avboitColorDesc.mDesc.mStructStride = sizeof(uint32_t);
    avboitColorDesc.mDesc.mSize = avboitColorDesc.mDesc.mElementCount * avboitColorDesc.mDesc.mStructStride;
    avboitColorDesc.pData = NULL;
    avboitColorDesc.ppBuffer = &pBufferAVBOITVolumeColor;
    addResource(&avboitColorDesc, NULL);''')

# Now add global pointers and remove old pointers
cpp_content = cpp_content.replace('Texture* pTextureAVBOITVolumeExtinction = NULL;', 'Buffer* pBufferAVBOITVolumeExtinction = NULL;')
cpp_content = cpp_content.replace('Texture* pTextureAVBOITVolumeColor = NULL;', 'Buffer* pBufferAVBOITVolumeColor = NULL;')

# Replace removal logic
cpp_content = cpp_content.replace('removeResource(pTextureAVBOITVolumeExtinction);', 'removeResource(pBufferAVBOITVolumeExtinction);')
cpp_content = cpp_content.replace('removeResource(pTextureAVBOITVolumeColor);', 'removeResource(pBufferAVBOITVolumeColor);')

# Replace descriptors logic updateDescriptorSet
cpp_content = cpp_content.replace('paramsAVBOITSplat[1].ppTextures = &pTextureAVBOITVolumeExtinction;', 'paramsAVBOITSplat[1].ppBuffers = &pBufferAVBOITVolumeExtinction;')
cpp_content = cpp_content.replace('paramsAVBOITSplat[2].ppTextures = &pTextureAVBOITVolumeColor;', 'paramsAVBOITSplat[2].ppBuffers = &pBufferAVBOITVolumeColor;')

cpp_content = cpp_content.replace('paramsAVBOITClear[0].ppTextures = &pTextureAVBOITVolumeExtinction;', 'paramsAVBOITClear[0].ppBuffers = &pBufferAVBOITVolumeExtinction;')
cpp_content = cpp_content.replace('paramsAVBOITClear[1].ppTextures = &pTextureAVBOITVolumeColor;', 'paramsAVBOITClear[1].ppBuffers = &pBufferAVBOITVolumeColor;')

cpp_content = cpp_content.replace('paramsAVBOITIntegrate[0].ppTextures = &pTextureAVBOITVolumeExtinction;', 'paramsAVBOITIntegrate[0].ppBuffers = &pBufferAVBOITVolumeExtinction;')
cpp_content = cpp_content.replace('paramsAVBOITIntegrate[2].ppTextures = &pTextureAVBOITVolumeColor;', 'paramsAVBOITIntegrate[2].ppBuffers = &pBufferAVBOITVolumeColor;')

# avboit composite uses SRV for extinction and color? If yes, it's ppBuffers now. But wait, we only use Lut SRV there!
# Wait! In updateDescriptorSet for Composite:
# paramsAVBOITComposite[0].ppTextures = &pTextureAVBOITVolumeExtinction;
cpp_content = cpp_content.replace('paramsAVBOITComposite[0].ppTextures = &pTextureAVBOITVolumeExtinction;', 'paramsAVBOITComposite[0].ppBuffers = &pBufferAVBOITVolumeExtinction;')
cpp_content = cpp_content.replace('paramsAVBOITComposite[2].ppTextures = &pTextureAVBOITVolumeColor;', 'paramsAVBOITComposite[2].ppBuffers = &pBufferAVBOITVolumeColor;')


# Now update the barriers in the render loop!
cpp_content = cpp_content.replace('''    TextureBarrier extBarrier = { pTextureAVBOITVolumeExtinction, RESOURCE_STATE_PIXEL_SHADER_RESOURCE, RESOURCE_STATE_UNORDERED_ACCESS };
    TextureBarrier colorBarrier = { pTextureAVBOITVolumeColor, RESOURCE_STATE_PIXEL_SHADER_RESOURCE, RESOURCE_STATE_UNORDERED_ACCESS };''',
'''    BufferBarrier extBarrier = { pBufferAVBOITVolumeExtinction, RESOURCE_STATE_PIXEL_SHADER_RESOURCE, RESOURCE_STATE_UNORDERED_ACCESS };
    BufferBarrier colorBarrier = { pBufferAVBOITVolumeColor, RESOURCE_STATE_PIXEL_SHADER_RESOURCE, RESOURCE_STATE_UNORDERED_ACCESS };''')

cpp_content = cpp_content.replace('''    TextureBarrier extBarrierSplat = { pTextureAVBOITVolumeExtinction, RESOURCE_STATE_UNORDERED_ACCESS, RESOURCE_STATE_PIXEL_SHADER_RESOURCE };
    TextureBarrier colorBarrierSplat = { pTextureAVBOITVolumeColor, RESOURCE_STATE_UNORDERED_ACCESS, RESOURCE_STATE_PIXEL_SHADER_RESOURCE };''',
'''    BufferBarrier extBarrierSplat = { pBufferAVBOITVolumeExtinction, RESOURCE_STATE_UNORDERED_ACCESS, RESOURCE_STATE_PIXEL_SHADER_RESOURCE };
    BufferBarrier colorBarrierSplat = { pBufferAVBOITVolumeColor, RESOURCE_STATE_UNORDERED_ACCESS, RESOURCE_STATE_PIXEL_SHADER_RESOURCE };''')


cpp_content = cpp_content.replace('TextureBarrier barriersClear[2] = { extBarrier, colorBarrier };', 'BufferBarrier barriersClear[2] = { extBarrier, colorBarrier };')
cpp_content = cpp_content.replace('cmdResourceBarrier(pCmd, 0, NULL, 2, barriersClear, 0, NULL);', 'cmdResourceBarrier(pCmd, 2, barriersClear, 0, NULL, 0, NULL);')

cpp_content = cpp_content.replace('TextureBarrier barriersSplat[3] = { extBarrierSplat, colorBarrierSplat, lutBarrierSplat };', 'BufferBarrier barriersSplatBuf[2] = { extBarrierSplat, colorBarrierSplat };\n    TextureBarrier barriersSplatTex[1] = { lutBarrierSplat };')
cpp_content = cpp_content.replace('cmdResourceBarrier(pCmd, 0, NULL, 3, barriersSplat, 0, NULL);', 'cmdResourceBarrier(pCmd, 2, barriersSplatBuf, 1, barriersSplatTex, 0, NULL);')

# Wait, the transition back to UAV for Splat pass!
cpp_content = cpp_content.replace('''    TextureBarrier extBarrierSplatStart = { pTextureAVBOITVolumeExtinction, RESOURCE_STATE_PIXEL_SHADER_RESOURCE, RESOURCE_STATE_UNORDERED_ACCESS };
    TextureBarrier colorBarrierSplatStart = { pTextureAVBOITVolumeColor, RESOURCE_STATE_PIXEL_SHADER_RESOURCE, RESOURCE_STATE_UNORDERED_ACCESS };''',
'''    BufferBarrier extBarrierSplatStart = { pBufferAVBOITVolumeExtinction, RESOURCE_STATE_PIXEL_SHADER_RESOURCE, RESOURCE_STATE_UNORDERED_ACCESS };
    BufferBarrier colorBarrierSplatStart = { pBufferAVBOITVolumeColor, RESOURCE_STATE_PIXEL_SHADER_RESOURCE, RESOURCE_STATE_UNORDERED_ACCESS };''')

cpp_content = cpp_content.replace('TextureBarrier barriersSplatStart[2] = { extBarrierSplatStart, colorBarrierSplatStart };', 'BufferBarrier barriersSplatStart[2] = { extBarrierSplatStart, colorBarrierSplatStart };')
cpp_content = cpp_content.replace('cmdResourceBarrier(pCmd, 0, NULL, 2, barriersSplatStart, 0, NULL);', 'cmdResourceBarrier(pCmd, 2, barriersSplatStart, 0, NULL, 0, NULL);')

with open(cpp_path, 'w', encoding='utf-8') as f:
    f.write(cpp_content)

print("Patch 15 applied.")
