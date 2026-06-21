import sys
import re

file_path = 'Examples_3/Unit_Tests/src/15_Transparency/15_Transparency.cpp'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# First, remove the wrongly placed pass_code at the top of the file
content = re.sub(r'^    void AdaptiveVoxelBasedOrderIndependentTransparencyPass\(Cmd\* pCmd\).*?    \}\n', '', content, flags=re.DOTALL)

pass_code = '''    void AdaptiveVoxelBasedOrderIndependentTransparencyPass(Cmd* pCmd)
    {
        uint32_t volWidth = pRenderTargetScreen->mWidth;
        uint32_t volHeight = pRenderTargetScreen->mHeight;
        uint32_t volDepth = 64; // Match AVBOIT_VOLUME_DEPTH

        BufferBarrier bufferBarriersUAV[] = {
            { pBufferAVBOITVolumeExtinction, RESOURCE_STATE_SHADER_RESOURCE, RESOURCE_STATE_UNORDERED_ACCESS }
        };
        TextureBarrier textureBarrierUAV[] = {
            { pTextureAVBOITVolumeTransmittanceLut, RESOURCE_STATE_SHADER_RESOURCE, RESOURCE_STATE_UNORDERED_ACCESS }
        };
        cmdResourceBarrier(pCmd, 1, bufferBarriersUAV, 1, textureBarrierUAV, 0, NULL);

        // 1. Clear Pass
        cmdBeginDebugMarker(pCmd, 1, 0, 1, "Clear AVBOIT");
        cmdBeginGpuTimestampQuery(pCmd, gCurrentGpuProfileToken, "Clear AVBOIT");
        cmdBindPipeline(pCmd, pPipelineAVBOITClear);
        cmdBindDescriptorSet(pCmd, 0, pDescriptorSetAVBOITClear);
        cmdDispatch(pCmd, (volWidth + 7) / 8, (volHeight + 7) / 8, (volDepth + 7) / 8);
        cmdEndGpuTimestampQuery(pCmd, gCurrentGpuProfileToken);
        cmdEndDebugMarker(pCmd);

        BufferBarrier barrierAfterClear[] = {
            { pBufferAVBOITVolumeExtinction, RESOURCE_STATE_UNORDERED_ACCESS, RESOURCE_STATE_UNORDERED_ACCESS }
        };
        cmdResourceBarrier(pCmd, 1, barrierAfterClear, 0, NULL, 0, NULL);

        // 2. Splat Pass
        cmdBeginDebugMarker(pCmd, 1, 0, 1, "Splat AVBOIT");
        cmdBeginGpuTimestampQuery(pCmd, gCurrentGpuProfileToken, "Splat AVBOIT");
        BindRenderTargetsDesc bindRenderTargets = {};
        bindRenderTargets.mDepthStencil = { pRenderTargetDepth, LOAD_ACTION_LOAD };
        cmdBindRenderTargets(pCmd, &bindRenderTargets);
        cmdSetViewport(pCmd, 0.0f, 0.0f, (float)pRenderTargetScreen->mWidth, (float)pRenderTargetScreen->mHeight, 0.0f, 1.0f);
        cmdSetScissor(pCmd, 0, 0, pRenderTargetScreen->mWidth, pRenderTargetScreen->mHeight);

        cmdBindPipeline(pCmd, pPipelineAVBOITSplat);
        cmdBindDescriptorSet(pCmd, 0, pDescriptorSetAVBOITSplat[0]);
        cmdBindDescriptorSet(pCmd, gFrameIndex, pDescriptorSetAVBOITSplat[1]);

        DrawObjects(pCmd, gTransparentDrawCallCount, gTransparentDrawCalls, pRootSignatureAVBOITSplat);

        cmdBindRenderTargets(pCmd, NULL);
        cmdEndGpuTimestampQuery(pCmd, gCurrentGpuProfileToken);
        cmdEndDebugMarker(pCmd);

        BufferBarrier barrierAfterSplat[] = {
            { pBufferAVBOITVolumeExtinction, RESOURCE_STATE_UNORDERED_ACCESS, RESOURCE_STATE_SHADER_RESOURCE }
        };
        cmdResourceBarrier(pCmd, 1, barrierAfterSplat, 0, NULL, 0, NULL);

        // 3. Integrate Pass
        cmdBeginDebugMarker(pCmd, 1, 0, 1, "Integrate AVBOIT");
        cmdBeginGpuTimestampQuery(pCmd, gCurrentGpuProfileToken, "Integrate AVBOIT");
        cmdBindPipeline(pCmd, pPipelineAVBOITIntegrate);
        cmdBindDescriptorSet(pCmd, 0, pDescriptorSetAVBOITIntegrate);
        cmdDispatch(pCmd, (volWidth + 7) / 8, (volHeight + 7) / 8, 1);
        cmdEndGpuTimestampQuery(pCmd, gCurrentGpuProfileToken);
        cmdEndDebugMarker(pCmd);

        // Transition back to SRV for composition
        TextureBarrier textureBarrierSRV[] = {
            { pTextureAVBOITVolumeTransmittanceLut, RESOURCE_STATE_UNORDERED_ACCESS, RESOURCE_STATE_SHADER_RESOURCE }
        };
        cmdResourceBarrier(pCmd, 0, NULL, 1, textureBarrierSRV, 0, NULL);

        // 4. Composite Pass (into render target)
        cmdBeginDebugMarker(pCmd, 1, 0, 1, "Composite AVBOIT");
        cmdBeginGpuTimestampQuery(pCmd, gCurrentGpuProfileToken, "Composite AVBOIT");
        
        BindRenderTargetsDesc bindRenderTargetsComp = {};
        bindRenderTargetsComp.mRenderTargetCount = 1;
        bindRenderTargetsComp.mRenderTargets[0] = { pRenderTargetScreen, LOAD_ACTION_LOAD };
        cmdBindRenderTargets(pCmd, &bindRenderTargetsComp);

        cmdBindPipeline(pCmd, pPipelineAVBOITComposite);
        cmdBindDescriptorSet(pCmd, 0, pDescriptorSetAVBOITComposite);
        cmdDraw(pCmd, 3, 0);

        cmdBindRenderTargets(pCmd, NULL);
        cmdEndGpuTimestampQuery(pCmd, gCurrentGpuProfileToken);
        cmdEndDebugMarker(pCmd);
    }'''

content = content.replace('void AdaptiveOrderIndependentTransparency(Cmd* pCmd)', pass_code + '\n\n    void AdaptiveOrderIndependentTransparency(Cmd* pCmd)')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 42 applied.")
