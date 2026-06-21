import sys

file_path = 'Examples_3/Unit_Tests/src/15_Transparency/15_Transparency.cpp'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Globals
if 'Shader* pShaderAVBOITForward = NULL;' not in content:
    content = content.replace('Shader* pShaderAVBOITComposite = NULL;', 'Shader* pShaderAVBOITComposite = NULL;\nShader* pShaderAVBOITForward = NULL;')
if 'Pipeline* pPipelineAVBOITForward = NULL;' not in content:
    content = content.replace('Pipeline* pPipelineAVBOITComposite = NULL;', 'Pipeline* pPipelineAVBOITComposite = NULL;\nPipeline* pPipelineAVBOITForward = NULL;')
if 'RootSignature* pRootSignatureAVBOITForward = NULL;' not in content:
    content = content.replace('RootSignature* pRootSignatureAVBOITComposite = NULL;', 'RootSignature* pRootSignatureAVBOITComposite = NULL;\nRootSignature* pRootSignatureAVBOITForward = NULL;')

# 2. Add Shaders
if 'avboitForwardShaderDesc.mStages[1] = { "avboit_forward.frag" };' not in content:
    add_shader_code = '''            ShaderLoadDesc avboitForwardShaderDesc = {};
            avboitForwardShaderDesc.mStages[0] = { "skybox.vert", NULL, 0, NULL, SHADER_STAGE_LOAD_FLAG_ENABLE_VR_MULTIVIEW };
            avboitForwardShaderDesc.mStages[1] = { "avboit_forward.frag", NULL, 0, NULL, SHADER_STAGE_LOAD_FLAG_ENABLE_VR_MULTIVIEW };
            addShader(pRenderer, &avboitForwardShaderDesc, &pShaderAVBOITForward);'''
    content = content.replace('addShader(pRenderer, &avboitCompositeShaderDesc, &pShaderAVBOITComposite);', 'addShader(pRenderer, &avboitCompositeShaderDesc, &pShaderAVBOITComposite);\n' + add_shader_code)
    
if 'removeShader(pRenderer, pShaderAVBOITForward);' not in content:
    content = content.replace('removeShader(pRenderer, pShaderAVBOITComposite);', 'removeShader(pRenderer, pShaderAVBOITComposite);\n            removeShader(pRenderer, pShaderAVBOITForward);')

# 3. RootSignature
if 'avboitForwardRootSignatureDesc.ppShaders = &pShaderAVBOITForward;' not in content:
    rs_code = '''            RootSignatureDesc avboitForwardRootSignatureDesc = {};
            avboitForwardRootSignatureDesc.mShaderCount = 1;
            avboitForwardRootSignatureDesc.ppShaders = &pShaderAVBOITForward;
            avboitForwardRootSignatureDesc.mMaxBindlessTextures = gScene->numMaterials;
            avboitForwardRootSignatureDesc.ppStaticSamplers = ppStaticSamplers;
            avboitForwardRootSignatureDesc.mStaticSamplerCount = gStaticSamplerCount;
            addRootSignature(pRenderer, &avboitForwardRootSignatureDesc, &pRootSignatureAVBOITForward);'''
    content = content.replace('addRootSignature(pRenderer, &avboitCompositeRootSignatureDesc, &pRootSignatureAVBOITComposite);', 'addRootSignature(pRenderer, &avboitCompositeRootSignatureDesc, &pRootSignatureAVBOITComposite);\n' + rs_code)

if 'removeRootSignature(pRenderer, pRootSignatureAVBOITForward);' not in content:
    content = content.replace('removeRootSignature(pRenderer, pRootSignatureAVBOITComposite);', 'removeRootSignature(pRenderer, pRootSignatureAVBOITComposite);\n            removeRootSignature(pRenderer, pRootSignatureAVBOITForward);')

# 4. Pipeline
if 'avboitForwardPipelineDesc' not in content:
    pipe_code = '''            GraphicsPipelineDesc& avboitForwardPipelineDesc = desc.mGraphicsDesc;
            avboitForwardPipelineDesc.mDepthStencilFormat = pRenderTargetDepth->mFormat;
            avboitForwardPipelineDesc.mRenderTargetCount = 1;
            avboitForwardPipelineDesc.pColorFormats = &pSwapChain->ppRenderTargets[0]->mFormat;
            avboitForwardPipelineDesc.mSampleCount = pSwapChain->ppRenderTargets[0]->mSampleCount;
            avboitForwardPipelineDesc.mSampleQuality = pSwapChain->ppRenderTargets[0]->mSampleQuality;
            avboitForwardPipelineDesc.mPrimitiveTopo = PRIMITIVE_TOPO_TRI_LIST;
            avboitForwardPipelineDesc.pShaderProgram = pShaderAVBOITForward;
            avboitForwardPipelineDesc.pRootSignature = pRootSignatureAVBOITForward;
            avboitForwardPipelineDesc.pVertexLayout = &vertexLayout;
            avboitForwardPipelineDesc.pRasterizerState = &rasterStateNoneDesc;
            
            DepthStateDesc forwardDepthStateDesc = {};
            forwardDepthStateDesc.mDepthTest = true;
            forwardDepthStateDesc.mDepthWrite = false;
            forwardDepthStateDesc.mDepthFunc = CMP_LEQUAL;
            avboitForwardPipelineDesc.pDepthState = &forwardDepthStateDesc;

            BlendStateDesc avboitForwardBlendState = {};
            avboitForwardBlendState.mSrcAlphaFactors[0] = BC_ZERO;
            avboitForwardBlendState.mDstAlphaFactors[0] = BC_ONE;
            avboitForwardBlendState.mSrcFactors[0] = BC_ONE;
            avboitForwardBlendState.mDstFactors[0] = BC_ONE;
            avboitForwardBlendState.mColorWriteMasks[0] = COLOR_MASK_ALL;
            avboitForwardBlendState.mRenderTargetMask = BLEND_STATE_TARGET_0;
            avboitForwardPipelineDesc.pBlendState = &avboitForwardBlendState;

            LOGF(eINFO, "Adding AVBOITForward Pipeline...");
            addPipeline(pRenderer, &desc, &pPipelineAVBOITForward);'''
    content = content.replace('addPipeline(pRenderer, &desc, &pPipelineAVBOITComposite);', 'addPipeline(pRenderer, &desc, &pPipelineAVBOITComposite);\n\n' + pipe_code)

if 'removePipeline(pRenderer, pPipelineAVBOITForward);' not in content:
    content = content.replace('removePipeline(pRenderer, pPipelineAVBOITComposite);', 'removePipeline(pRenderer, pPipelineAVBOITComposite);\n            removePipeline(pRenderer, pPipelineAVBOITForward);')

# 5. Composite Blend State
content = content.replace('avboitBlendState.mSrcFactors[0] = BC_ONE;', 'avboitBlendState.mSrcFactors[0] = BC_ZERO;')
content = content.replace('avboitBlendState.mDstFactors[0] = BC_ONE_MINUS_SRC_ALPHA;', 'avboitBlendState.mDstFactors[0] = BC_SRC_COLOR;')

# 6. Render Pass
if 'Forward AVBOIT' not in content:
    pass_code = '''        // 5. Forward Pass (Draw transparent objects again with colors)
        cmdBeginDebugMarker(pCmd, 1, 0, 1, "Forward AVBOIT");
        cmdBeginGpuTimestampQuery(pCmd, gCurrentGpuProfileToken, "Forward AVBOIT");
        
        BindRenderTargetsDesc bindRenderTargetsFwd = {};
        bindRenderTargetsFwd.mRenderTargetCount = 1;
        bindRenderTargetsFwd.mRenderTargets[0] = { pRenderTargetScreen, LOAD_ACTION_LOAD };
        bindRenderTargetsFwd.mDepthStencil = { pRenderTargetDepth, LOAD_ACTION_LOAD };
        cmdBindRenderTargets(pCmd, &bindRenderTargetsFwd);

        cmdBindPipeline(pCmd, pPipelineAVBOITForward);
        // Wait, what descriptor sets does the Forward pass use?
        // It uses the same set 0 and 1 as Splat pass, because it has the same layout plus TransmittanceLUT.
        // Wait, Splat uses AVBOITSplat descriptors. Forward should use AVBOITSplat descriptors?
        // Actually, Forward needs Transmittance LUT SRV. Splat does NOT have Transmittance LUT SRV.
        // Let's bind pDescriptorSetAVBOITSplat[0] and [1], BUT we need to update the shader!
        // The Root Signature of AVBOITForward is independent. We need to create pDescriptorSetAVBOITForward[2].
'''
    # Wait, instead of doing this via python directly, I'll write the python to generate a patch.

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 48 partial applied.")
