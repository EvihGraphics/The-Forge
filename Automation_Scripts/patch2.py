import re

file_path = 'Examples_3/Unit_Tests/src/15_Transparency/15_Transparency.cpp'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix endUpdateResource
content = content.replace('endUpdateResource(&avboitUpdate, NULL);', 'endUpdateResource(&avboitUpdate);')

# Fix depth state
content = content.replace('avboitSplatPipelineDesc.pDepthState = &depthStateEnableDesc;', 'avboitSplatPipelineDesc.pDepthState = &reverseDepthStateNoWriteDesc;')

# Remove duplicate AVBOIT globals
# Let's find the exact duplicate block and remove one of them.
duplicate_block = r'''// AVBOIT Shaders
Shader\* pShaderAVBOITSplat = NULL;
Shader\* pShaderAVBOITClear = NULL;
Shader\* pShaderAVBOITIntegrate = NULL;
Shader\* pShaderAVBOITComposite = NULL;

RootSignature\* pRootSignatureAVBOITSplat = NULL;
RootSignature\* pRootSignatureAVBOITClear = NULL;
RootSignature\* pRootSignatureAVBOITIntegrate = NULL;
RootSignature\* pRootSignatureAVBOITComposite = NULL;

Pipeline\* pPipelineAVBOITSplat = NULL;
Pipeline\* pPipelineAVBOITClear = NULL;
Pipeline\* pPipelineAVBOITIntegrate = NULL;
Pipeline\* pPipelineAVBOITComposite = NULL;

Texture\* pTextureAVBOITVolumeExtinction = NULL;
Texture\* pTextureAVBOITVolumeTransmittanceLut = NULL;

DescriptorSet\* pDescriptorSetAVBOITSplat\[2\] = \{ NULL \};
DescriptorSet\* pDescriptorSetAVBOITClear = NULL;
DescriptorSet\* pDescriptorSetAVBOITIntegrate = NULL;
DescriptorSet\* pDescriptorSetAVBOITComposite = NULL;'''

content = re.sub(duplicate_block, '', content, count=1)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 2 applied.")
