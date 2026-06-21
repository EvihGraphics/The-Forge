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
    match = matches[0]
    content = content[:match.end()] + "\n" + new_code + content[match.end():]
    print(f"Injected successfully after {pattern.strip()[:30]}")

inject(r'Shader\* pShaderAOITClear = NULL;', '''
// AVBOIT Shaders
Shader* pShaderAVBOITSplat = NULL;
Shader* pShaderAVBOITClear = NULL;
Shader* pShaderAVBOITIntegrate = NULL;
Shader* pShaderAVBOITComposite = NULL;

RootSignature* pRootSignatureAVBOITSplat = NULL;
RootSignature* pRootSignatureAVBOITClear = NULL;
RootSignature* pRootSignatureAVBOITIntegrate = NULL;
RootSignature* pRootSignatureAVBOITComposite = NULL;

Pipeline* pPipelineAVBOITSplat = NULL;
Pipeline* pPipelineAVBOITClear = NULL;
Pipeline* pPipelineAVBOITIntegrate = NULL;
Pipeline* pPipelineAVBOITComposite = NULL;

Texture* pTextureAVBOITVolumeExtinction = NULL;
Texture* pTextureAVBOITVolumeTransmittanceLut = NULL;

DescriptorSet* pDescriptorSetAVBOITSplat[2] = { NULL };
DescriptorSet* pDescriptorSetAVBOITClear = NULL;
DescriptorSet* pDescriptorSetAVBOITIntegrate = NULL;
DescriptorSet* pDescriptorSetAVBOITComposite = NULL;
''')

inject(r'addShader\(pRenderer, &aoitClearShaderDesc, &pShaderAOITClear\);\n        }', '''
        ShaderLoadDesc avboitSplatShaderDesc = {};
        avboitSplatShaderDesc.mStages[0] = { "forward.vert", NULL, 0 };
        avboitSplatShaderDesc.mStages[1] = { "AVBOIT.frag", NULL, 0 };
        addShader(pRenderer, &avboitSplatShaderDesc, &pShaderAVBOITSplat);

        ShaderLoadDesc avboitClearShaderDesc = {};
        avboitClearShaderDesc.mStages[0] = { "avboit_clear.comp", NULL, 0 };
        addShader(pRenderer, &avboitClearShaderDesc, &pShaderAVBOITClear);

        ShaderLoadDesc avboitIntegrateShaderDesc = {};
        avboitIntegrateShaderDesc.mStages[0] = { "avboit_integrate.comp", NULL, 0 };
        addShader(pRenderer, &avboitIntegrateShaderDesc, &pShaderAVBOITIntegrate);

        ShaderLoadDesc avboitCompositeShaderDesc = {};
        avboitCompositeShaderDesc.mStages[0] = { "fullscreen.vert", NULL, 0 };
        avboitCompositeShaderDesc.mStages[1] = { "avboit_composite.frag", NULL, 0 };
        addShader(pRenderer, &avboitCompositeShaderDesc, &pShaderAVBOITComposite);
''')

inject(r'removeShader\(pRenderer, pShaderAOITClear\);', '''
            removeShader(pRenderer, pShaderAVBOITSplat);
            removeShader(pRenderer, pShaderAVBOITClear);
            removeShader(pRenderer, pShaderAVBOITIntegrate);
            removeShader(pRenderer, pShaderAVBOITComposite);
''')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Injection Phase 1 complete.")
