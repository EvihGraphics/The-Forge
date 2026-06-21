import re

path = 'Examples_3/Unit_Tests/src/15_Transparency/15_Transparency.cpp'

# Read the checkpoint version
with open(r'D:\Users\l3d\Documents\AVBOIT\The-Forge-clean-checkpoint\Examples_3\Unit_Tests\src\15_Transparency\15_Transparency.cpp', 'r', encoding='utf-8') as f:
    content = f.read()

# Inject the Uniform Update
target1 = r'''        uint32_t volDepth = 64; // Match AVBOIT_VOLUME_DEPTH



        BufferBarrier bufferBarriersUAV\[\] = {'''
replacement1 = r'''        uint32_t volDepth = 64; // Match AVBOIT_VOLUME_DEPTH

        // Update AVBOIT Uniforms
        uint32_t avboitUniformData[4] = { volWidth, volHeight, volDepth, 0 };
        BufferUpdateDesc avboitUpdate = { pBufferAVBOITUniform[gFrameIndex] };
        beginUpdateResource(&avboitUpdate);
        memcpy(avboitUpdate.pMappedData, avboitUniformData, sizeof(avboitUniformData));
        endUpdateResource(&avboitUpdate);

        BufferBarrier bufferBarriersUAV[] = {'''

content = re.sub(target1, replacement1, content)

# Inject the Forward Color Pass
target2 = r'''        cmdBindRenderTargets\(pCmd, NULL\);
        cmdEndGpuTimestampQuery\(pCmd, gCurrentGpuProfileToken\);
        cmdEndDebugMarker\(pCmd\);
    }

    void AdaptiveOrderIndependentTransparency\(Cmd\* pCmd\)'''
replacement2 = r'''        cmdBindRenderTargets(pCmd, NULL);
        cmdEndGpuTimestampQuery(pCmd, gCurrentGpuProfileToken);
        cmdEndDebugMarker(pCmd);

        // 5. Forward Color Pass (draw transparent objects with actual colors)
        cmdBeginDebugMarker(pCmd, 1, 0, 1, "Forward AVBOIT");
        cmdBeginGpuTimestampQuery(pCmd, gCurrentGpuProfileToken, "Forward AVBOIT");

        BindRenderTargetsDesc bindRenderTargetsFwd = {};
        bindRenderTargetsFwd.mRenderTargetCount = 1;
        bindRenderTargetsFwd.mRenderTargets[0] = { pRenderTargetScreen, LOAD_ACTION_LOAD };
        bindRenderTargetsFwd.mDepthStencil = { pRenderTargetDepth, LOAD_ACTION_LOAD };
        cmdBindRenderTargets(pCmd, &bindRenderTargetsFwd);
        cmdSetViewport(pCmd, 0.0f, 0.0f, (float)pRenderTargetScreen->mWidth, (float)pRenderTargetScreen->mHeight, 0.0f, 1.0f);
        cmdSetScissor(pCmd, 0, 0, pRenderTargetScreen->mWidth, pRenderTargetScreen->mHeight);

        cmdBindPipeline(pCmd, pPipelineAVBOITForward);
        cmdBindDescriptorSet(pCmd, 0, pDescriptorSetAVBOITForward[0]);
        cmdBindDescriptorSet(pCmd, gFrameIndex, pDescriptorSetAVBOITForward[1]);
        DrawObjects(pCmd, gTransparentDrawCallCount, gTransparentDrawCalls, pRootSignatureAVBOITForward);

        cmdBindRenderTargets(pCmd, NULL);
        cmdEndGpuTimestampQuery(pCmd, gCurrentGpuProfileToken);
        cmdEndDebugMarker(pCmd);
    }

    void AdaptiveOrderIndependentTransparency(Cmd* pCmd)'''

content = re.sub(target2, replacement2, content)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied fixes to 15_Transparency.cpp!")
