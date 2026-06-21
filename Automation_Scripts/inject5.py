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

inject(r'addPipeline\(pRenderer, &desc, &pPipelineAOITClear\);\n        }', '''
        // AVBOIT Pipelines
        {
            PipelineDesc desc = {};
            desc.mType = PIPELINE_TYPE_GRAPHICS;
            GraphicsPipelineDesc& avboitSplatPipelineDesc = desc.mGraphicsDesc;
            avboitSplatPipelineDesc.mDepthStencilFormat = pRenderTargetDepth->mFormat;
            avboitSplatPipelineDesc.mRenderTargetCount = 0; // AVBOIT Splat doesn't write to RenderTargets, only UAVs
            avboitSplatPipelineDesc.mSampleCount = pRenderTargetDepth->mSampleCount;
            avboitSplatPipelineDesc.mSampleQuality = pRenderTargetDepth->mSampleQuality;
            avboitSplatPipelineDesc.mPrimitiveTopo = PRIMITIVE_TOPO_TRI_LIST;
            avboitSplatPipelineDesc.pShaderProgram = pShaderAVBOITSplat;
            avboitSplatPipelineDesc.pRootSignature = pRootSignatureAVBOITSplat;
            avboitSplatPipelineDesc.pVertexLayout = &vertexLayoutDefault;
            avboitSplatPipelineDesc.pRasterizerState = &rasterStateNoneDesc;
            avboitSplatPipelineDesc.pDepthState = &depthStateDesc;
            avboitSplatPipelineDesc.pBlendState = NULL;
            addPipeline(pRenderer, &desc, &pPipelineAVBOITSplat);

            desc.mType = PIPELINE_TYPE_COMPUTE;
            ComputePipelineDesc& avboitClearPipelineDesc = desc.mComputeDesc;
            avboitClearPipelineDesc.pShaderProgram = pShaderAVBOITClear;
            avboitClearPipelineDesc.pRootSignature = pRootSignatureAVBOITClear;
            addPipeline(pRenderer, &desc, &pPipelineAVBOITClear);

            ComputePipelineDesc& avboitIntegratePipelineDesc = desc.mComputeDesc;
            avboitIntegratePipelineDesc.pShaderProgram = pShaderAVBOITIntegrate;
            avboitIntegratePipelineDesc.pRootSignature = pRootSignatureAVBOITIntegrate;
            addPipeline(pRenderer, &desc, &pPipelineAVBOITIntegrate);

            desc.mType = PIPELINE_TYPE_GRAPHICS;
            GraphicsPipelineDesc& avboitCompositePipelineDesc = desc.mGraphicsDesc;
            avboitCompositePipelineDesc.mDepthStencilFormat = TinyImageFormat_UNDEFINED;
            avboitCompositePipelineDesc.mRenderTargetCount = 1;
            avboitCompositePipelineDesc.pColorFormats = &pRenderTargetScreen->mFormat;
            avboitCompositePipelineDesc.mSampleCount = pRenderTargetScreen->mSampleCount;
            avboitCompositePipelineDesc.mSampleQuality = pRenderTargetScreen->mSampleQuality;
            avboitCompositePipelineDesc.mPrimitiveTopo = PRIMITIVE_TOPO_TRI_LIST;
            avboitCompositePipelineDesc.pShaderProgram = pShaderAVBOITComposite;
            avboitCompositePipelineDesc.pRootSignature = pRootSignatureAVBOITComposite;
            avboitCompositePipelineDesc.pVertexLayout = NULL;
            avboitCompositePipelineDesc.pRasterizerState = &rasterStateNoneDesc;
            avboitCompositePipelineDesc.pDepthState = &depthStateDisabledDesc;
            BlendStateDesc avboitBlendState = {};
            avboitBlendState.mSrcAlphaFactors[0] = BC_ZERO;
            avboitBlendState.mDstAlphaFactors[0] = BC_ONE;
            avboitBlendState.mSrcFactors[0] = BC_ONE;
            avboitBlendState.mDstFactors[0] = BC_ONE_MINUS_SRC_ALPHA;
            avboitBlendState.mColorWriteMasks[0] = COLOR_MASK_ALL;
            avboitBlendState.mRenderTargetMask = BLEND_STATE_TARGET_0;
            avboitBlendState.mIndependentBlend = false;
            avboitCompositePipelineDesc.pBlendState = &avboitBlendState;
            addPipeline(pRenderer, &desc, &pPipelineAVBOITComposite);
        }
''')

inject(r'removePipeline\(pRenderer, pPipelineAOITClear\);\n        }', '''
        {
            removePipeline(pRenderer, pPipelineAVBOITSplat);
            removePipeline(pRenderer, pPipelineAVBOITClear);
            removePipeline(pRenderer, pPipelineAVBOITIntegrate);
            removePipeline(pRenderer, pPipelineAVBOITComposite);
        }
''')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Injection Phase 4 complete.")
