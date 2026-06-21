import sys

file_path = 'Examples_3/Unit_Tests/src/15_Transparency/15_Transparency.cpp'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('avboitCompositePipelineDesc.pColorFormats = &pRenderTargetScreen->mFormat;', 'avboitCompositePipelineDesc.pColorFormats = &pSwapChain->ppRenderTargets[0]->mFormat;')
content = content.replace('avboitCompositePipelineDesc.mSampleCount = pRenderTargetScreen->mSampleCount;', 'avboitCompositePipelineDesc.mSampleCount = pSwapChain->ppRenderTargets[0]->mSampleCount;')
content = content.replace('avboitCompositePipelineDesc.mSampleQuality = pRenderTargetScreen->mSampleQuality;', 'avboitCompositePipelineDesc.mSampleQuality = pSwapChain->ppRenderTargets[0]->mSampleQuality;')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 28 applied.")
