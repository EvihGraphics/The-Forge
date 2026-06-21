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

inject(r'addRootSignature\(pRenderer, &aoitClearRootSignatureDesc, &pRootSignatureAOITClear\);', '''
            // AVBOIT Root Signatures
            RootSignatureDesc avboitSplatRSDesc = {};
            avboitSplatRSDesc.ppShaders = &pShaderAVBOITSplat;
            avboitSplatRSDesc.mShaderCount = 1;
            avboitSplatRSDesc.mMaxBindlessTextures = 0;
            const char* splatSamplers[] = { "PointSampler", "BilinearSampler" };
            Sampler* splatSamplersPtr[] = { pSamplerPointClamp, pSamplerBilinear };
            avboitSplatRSDesc.mStaticSamplerCount = 2;
            avboitSplatRSDesc.ppStaticSamplerNames = splatSamplers;
            avboitSplatRSDesc.ppStaticSamplers = splatSamplersPtr;
            addRootSignature(pRenderer, &avboitSplatRSDesc, &pRootSignatureAVBOITSplat);

            RootSignatureDesc avboitClearRSDesc = {};
            avboitClearRSDesc.ppShaders = &pShaderAVBOITClear;
            avboitClearRSDesc.mShaderCount = 1;
            addRootSignature(pRenderer, &avboitClearRSDesc, &pRootSignatureAVBOITClear);

            RootSignatureDesc avboitIntegrateRSDesc = {};
            avboitIntegrateRSDesc.ppShaders = &pShaderAVBOITIntegrate;
            avboitIntegrateRSDesc.mShaderCount = 1;
            addRootSignature(pRenderer, &avboitIntegrateRSDesc, &pRootSignatureAVBOITIntegrate);

            RootSignatureDesc avboitCompositeRSDesc = {};
            avboitCompositeRSDesc.ppShaders = &pShaderAVBOITComposite;
            avboitCompositeRSDesc.mShaderCount = 1;
            addRootSignature(pRenderer, &avboitCompositeRSDesc, &pRootSignatureAVBOITComposite);
''')

inject(r'removeRootSignature\(pRenderer, pRootSignatureAOITClear\);', '''
        removeRootSignature(pRenderer, pRootSignatureAVBOITSplat);
        removeRootSignature(pRenderer, pRootSignatureAVBOITClear);
        removeRootSignature(pRenderer, pRootSignatureAVBOITIntegrate);
        removeRootSignature(pRenderer, pRootSignatureAVBOITComposite);
''')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Injection Phase 2 complete.")
