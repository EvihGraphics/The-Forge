import sys
import re

file_path = 'Examples_3/Unit_Tests/src/15_Transparency/15_Transparency.cpp'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Globals
if 'DescriptorSet* pDescriptorSetAVBOITForward[2] = { NULL };' not in content:
    content = content.replace('DescriptorSet* pDescriptorSetAVBOITSplat[2] = { NULL };', 'DescriptorSet* pDescriptorSetAVBOITSplat[2] = { NULL };\nDescriptorSet* pDescriptorSetAVBOITForward[2] = { NULL };')

# 2. Add DescriptorSet
if 'addDescriptorSet(pRenderer, &setDesc, &pDescriptorSetAVBOITForward[0]);' not in content:
    add_desc = '''            setDesc = {}; setDesc.pRootSignature = pRootSignatureAVBOITForward; setDesc.mUpdateFrequency = DESCRIPTOR_UPDATE_FREQ_NONE; setDesc.mMaxSets = 1;
            addDescriptorSet(pRenderer, &setDesc, &pDescriptorSetAVBOITForward[0]);
            setDesc = {}; setDesc.pRootSignature = pRootSignatureAVBOITForward; setDesc.mUpdateFrequency = DESCRIPTOR_UPDATE_FREQ_PER_FRAME; setDesc.mMaxSets = gDataBufferCount;
            addDescriptorSet(pRenderer, &setDesc, &pDescriptorSetAVBOITForward[1]);'''
    content = content.replace('addDescriptorSet(pRenderer, &setDesc, &pDescriptorSetAVBOITSplat[1]);', 'addDescriptorSet(pRenderer, &setDesc, &pDescriptorSetAVBOITSplat[1]);\n' + add_desc)

# 3. Remove DescriptorSet
if 'removeDescriptorSet(pRenderer, pDescriptorSetAVBOITForward[0]);' not in content:
    rm_desc = '''            removeDescriptorSet(pRenderer, pDescriptorSetAVBOITForward[0]);
            removeDescriptorSet(pRenderer, pDescriptorSetAVBOITForward[1]);'''
    content = content.replace('removeDescriptorSet(pRenderer, pDescriptorSetAVBOITSplat[1]);', 'removeDescriptorSet(pRenderer, pDescriptorSetAVBOITSplat[1]);\n' + rm_desc)

# 4. Update DescriptorSet
if 'avboitForwardParams[0].ppTextures = &pTextureAVBOITVolumeTransmittanceLut;' not in content:
    upd_desc = '''            DescriptorData avboitForwardParams[1] = {};
            avboitForwardParams[0].pName = "VolumeTransmittanceLutSRV";
            avboitForwardParams[0].ppTextures = &pTextureAVBOITVolumeTransmittanceLut;
            updateDescriptorSet(pRenderer, 0, pDescriptorSetAVBOITForward[0], 1, avboitForwardParams);'''
    content = content.replace('updateDescriptorSet(pRenderer, 0, pDescriptorSetAVBOITSplat[0], 1, avboitSplatParams);', 'updateDescriptorSet(pRenderer, 0, pDescriptorSetAVBOITSplat[0], 1, avboitSplatParams);\n' + upd_desc)

if 'updateDescriptorSet(pRenderer, i, pDescriptorSetAVBOITForward[1], 1, avboitSplatFrameParams);' not in content:
    content = content.replace('updateDescriptorSet(pRenderer, i, pDescriptorSetAVBOITSplat[1], 1, avboitSplatFrameParams);', 'updateDescriptorSet(pRenderer, i, pDescriptorSetAVBOITSplat[1], 1, avboitSplatFrameParams);\n                updateDescriptorSet(pRenderer, i, pDescriptorSetAVBOITForward[1], 1, avboitSplatFrameParams);')

# 5. Add Forward Draw Pass
if 'cmdBeginDebugMarker(pCmd, 1, 0, 1, "Forward AVBOIT");' not in content:
    pass_code = '''        // 5. Forward Pass (Draw transparent objects again with colors)
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
'''
    content = re.sub(r'(cmdEndDebugMarker\(pCmd\);\n    \})', pass_code + r'\1', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 49 applied.")
