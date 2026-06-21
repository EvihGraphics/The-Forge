import re
import sys

file_path = 'Examples_3/Unit_Tests/src/15_Transparency/15_Transparency.cpp'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

def replace_block(pattern, new_code):
    global content
    matches = list(re.finditer(pattern, content, re.MULTILINE | re.DOTALL))
    if not matches:
        print(f"Failed to find pattern: {pattern}")
        sys.exit(1)
    match = matches[-1]
    content = content[:match.start()] + new_code + content[match.end():]
    print(f"Replaced successfully {pattern.strip()[:30]}")

replace_block(r'void AdaptiveVoxelBasedOITPass\(Cmd\* pCmd\)\s*\{\s*// Placeholder for AVBOIT Pass\s*\}', '''void AdaptiveVoxelBasedOITPass(Cmd* pCmd)
{
    // Update AVBOIT Uniforms
    uint32_t avboitUniformData[4] = { 1920, 1080, 64, 0 };
    BufferUpdateDesc avboitUpdate = { pBufferAVBOITUniform[gFrameIndex] };
    beginUpdateResource(&avboitUpdate);
    memcpy(avboitUpdate.pMappedData, avboitUniformData, sizeof(avboitUniformData));
    endUpdateResource(&avboitUpdate, NULL);

    // Barrier: UAV for Clear
    TextureBarrier clearBarriers[] = {
        { pTextureAVBOITVolumeExtinction, RESOURCE_STATE_PIXEL_SHADER_RESOURCE, RESOURCE_STATE_UNORDERED_ACCESS },
        { pTextureAVBOITVolumeTransmittanceLut, RESOURCE_STATE_PIXEL_SHADER_RESOURCE, RESOURCE_STATE_UNORDERED_ACCESS }
    };
    cmdResourceBarrier(pCmd, 0, NULL, 2, clearBarriers, 0, NULL);

    // 1. Clear Pass
    cmdBindPipeline(pCmd, pPipelineAVBOITClear);
    cmdBindDescriptorSet(pCmd, 0, pDescriptorSetAVBOITClear);
    uint32_t threadGroupX = (1920 + 7) / 8;
    uint32_t threadGroupY = (1080 + 7) / 8;
    uint32_t threadGroupZ = (64 + 7) / 8;
    cmdDispatch(pCmd, threadGroupX, threadGroupY, threadGroupZ);

    // Barrier: UAV to UAV (Wait for clear to finish)
    TextureBarrier splatBarriers[] = {
        { pTextureAVBOITVolumeExtinction, RESOURCE_STATE_UNORDERED_ACCESS, RESOURCE_STATE_UNORDERED_ACCESS }
    };
    cmdResourceBarrier(pCmd, 0, NULL, 1, splatBarriers, 0, NULL);

    // 2. Splat Pass (Draw transparent objects)
    cmdBindPipeline(pCmd, pPipelineAVBOITSplat);
    cmdBindDescriptorSet(pCmd, 0, pDescriptorSetAVBOITSplat[0]);
    cmdBindDescriptorSet(pCmd, gFrameIndex, pDescriptorSetAVBOITSplat[1]);
    
    // Draw all transparent objects
    for (uint32_t i = 0; i < gTransparentDrawCallCount; ++i)
    {
        DrawCall* dc = &gTransparentDrawCalls[i];
        cmdBindDescriptorSet(pCmd, dc->mDrawIdx, pDescriptorSetTextureBinding);
        cmdBindDescriptorSet(pCmd, dc->mDrawIdx, pDescriptorSetUniforms);
        cmdBindVertexBuffer(pCmd, 1, &pMeshes[dc->mMeshIdx]->pVertexBuffers[0], pMeshes[dc->mMeshIdx]->mVertexStrides, NULL);
        if (pMeshes[dc->mMeshIdx]->pIndexBuffer != NULL)
        {
            cmdBindIndexBuffer(pCmd, pMeshes[dc->mMeshIdx]->pIndexBuffer, pMeshes[dc->mMeshIdx]->mIndexType, 0);
            cmdDrawIndexed(pCmd, dc->mIndexCount, dc->mStartIndex, 0);
        }
        else
        {
            cmdDraw(pCmd, dc->mVertexCount, 0);
        }
    }

    // Barrier: Splat done, prepare for Integrate
    TextureBarrier integrateBarriers[] = {
        { pTextureAVBOITVolumeExtinction, RESOURCE_STATE_UNORDERED_ACCESS, RESOURCE_STATE_PIXEL_SHADER_RESOURCE }
    };
    cmdResourceBarrier(pCmd, 0, NULL, 1, integrateBarriers, 0, NULL);

    // 3. Integrate Pass
    cmdBindPipeline(pCmd, pPipelineAVBOITIntegrate);
    cmdBindDescriptorSet(pCmd, 0, pDescriptorSetAVBOITIntegrate);
    cmdDispatch(pCmd, threadGroupX, threadGroupY, 1);

    // Barrier: Integrate done, prepare for Composite
    TextureBarrier compositeBarriers[] = {
        { pTextureAVBOITVolumeTransmittanceLut, RESOURCE_STATE_UNORDERED_ACCESS, RESOURCE_STATE_PIXEL_SHADER_RESOURCE }
    };
    cmdResourceBarrier(pCmd, 0, NULL, 1, compositeBarriers, 0, NULL);

    // 4. Composite Pass
    cmdBindPipeline(pCmd, pPipelineAVBOITComposite);
    cmdBindDescriptorSet(pCmd, 0, pDescriptorSetAVBOITComposite);
    cmdDraw(pCmd, 3, 0);

    // End: keep states as SRV
}''')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Injection Phase 6 complete.")
