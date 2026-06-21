import sys

file_path = 'Examples_3/Unit_Tests/src/15_Transparency/15_Transparency.cpp'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('''            RootSignatureDesc avboitSplatRSDesc = {};
            avboitSplatRSDesc.ppShaders = &pShaderAVBOITSplat;
            avboitSplatRSDesc.mShaderCount = 1;
            const char* splatSamplers[] = { "PointSampler", "BilinearSampler" };
            Sampler* splatSamplersPtr[] = { pSamplerPointClamp, pSamplerBilinear };
            avboitSplatRSDesc.mStaticSamplerCount = 2;
            avboitSplatRSDesc.ppStaticSamplerNames = splatSamplers;
            avboitSplatRSDesc.ppStaticSamplers = splatSamplersPtr;
            addRootSignature(pRenderer, &avboitSplatRSDesc, &pRootSignatureAVBOITSplat);''',
'''            RootSignatureDesc avboitSplatRSDesc = {};
            avboitSplatRSDesc.ppShaders = &pShaderAVBOITSplat;
            avboitSplatRSDesc.mShaderCount = 1;
            avboitSplatRSDesc.ppStaticSamplers = staticSamplers;
            avboitSplatRSDesc.mStaticSamplerCount = numStaticSamplers;
            avboitSplatRSDesc.ppStaticSamplerNames = staticSamplerNames;
            avboitSplatRSDesc.mMaxBindlessTextures = TEXTURE_COUNT;
            addRootSignature(pRenderer, &avboitSplatRSDesc, &pRootSignatureAVBOITSplat);''')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 31 applied.")
