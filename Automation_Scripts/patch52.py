import sys

file_path = 'Examples_3/Unit_Tests/src/15_Transparency/15_Transparency.cpp'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

rs_code = '''            RootSignatureDesc avboitForwardRootSignatureDesc = {};
            avboitForwardRootSignatureDesc.mShaderCount = 1;
            avboitForwardRootSignatureDesc.ppShaders = &pShaderAVBOITForward;
            avboitForwardRootSignatureDesc.mMaxBindlessTextures = gScene->numMaterials;
            avboitForwardRootSignatureDesc.ppStaticSamplers = ppStaticSamplers;
            avboitForwardRootSignatureDesc.ppStaticSamplerNames = pStaticSamplerNames;
            avboitForwardRootSignatureDesc.mStaticSamplerCount = gStaticSamplerCount;
            addRootSignature(pRenderer, &avboitForwardRootSignatureDesc, &pRootSignatureAVBOITForward);'''

content = content.replace('addRootSignature(pRenderer, &avboitCompositeRSDesc, &pRootSignatureAVBOITComposite);', 'addRootSignature(pRenderer, &avboitCompositeRSDesc, &pRootSignatureAVBOITComposite);\n' + rs_code)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 52 applied.")
