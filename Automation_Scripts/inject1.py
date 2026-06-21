import re

with open('Examples_3/Unit_Tests/src/15_Transparency/15_Transparency.cpp', 'r', encoding='utf-8') as f:
    content = f.read()

def inject_after(pattern, new_code):
    global content
    matches = list(re.finditer(pattern, content))
    if not matches:
        print(f"Failed to find: {pattern}")
    else:
        match = matches[-1] # use the last match to be safe, or specify
        content = content[:match.end()] + "\n" + new_code + content[match.end():]
        print(f"Injected after: {pattern.strip()}")

# 1. Globals
inject_after(r'Buffer\*\s+pBufferAOITColorData;', '''
/************************************************************************/
// AVBOIT Resources
/************************************************************************/
Texture* pTextureAVBOITVolumeExtinction = NULL;
Texture* pTextureAVBOITVolumeTransmittanceLut = NULL;

Shader* pShaderAVBOITSplat = NULL;
Pipeline* pPipelineAVBOITSplat = NULL;
RootSignature* pRootSignatureAVBOITSplat = NULL;
DescriptorSet* pDescriptorSetAVBOITSplat = NULL;

Shader* pShaderAVBOITClear = NULL;
Pipeline* pPipelineAVBOITClear = NULL;
RootSignature* pRootSignatureAVBOITClear = NULL;
DescriptorSet* pDescriptorSetAVBOITClear = NULL;

Shader* pShaderAVBOITIntegrate = NULL;
Pipeline* pPipelineAVBOITIntegrate = NULL;
RootSignature* pRootSignatureAVBOITIntegrate = NULL;
DescriptorSet* pDescriptorSetAVBOITIntegrate = NULL;

Shader* pShaderAVBOITComposite = NULL;
Pipeline* pPipelineAVBOITComposite = NULL;
RootSignature* pRootSignatureAVBOITComposite = NULL;
DescriptorSet* pDescriptorSetAVBOITComposite = NULL;
''')

# 2. Init() Shaders
inject_after(r'addShader\(pRenderer, &aoitCompositeDesc, &pShaderAOITComposite\);', '''
        ShaderLoadDesc avboitSplatDesc = {};
        avboitSplatDesc.mStages[0] = { "forward.vert", NULL, 0 };
        avboitSplatDesc.mStages[1] = { "AVBOIT.frag", NULL, 0 };
        addShader(pRenderer, &avboitSplatDesc, &pShaderAVBOITSplat);

        ShaderLoadDesc avboitClearDesc = {};
        avboitClearDesc.mStages[0] = { "avboit_clear.comp", NULL, 0 };
        addShader(pRenderer, &avboitClearDesc, &pShaderAVBOITClear);

        ShaderLoadDesc avboitIntegrateDesc = {};
        avboitIntegrateDesc.mStages[0] = { "avboit_integrate.comp", NULL, 0 };
        addShader(pRenderer, &avboitIntegrateDesc, &pShaderAVBOITIntegrate);
''')

with open('Examples_3/Unit_Tests/src/15_Transparency/15_Transparency.cpp', 'w', encoding='utf-8') as f:
    f.write(content)
print("Injection Phase 1 complete.")
