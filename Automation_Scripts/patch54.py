import sys

file_path = 'Examples_3/Unit_Tests/src/15_Transparency/15_Transparency.cpp'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('avboitForwardRootSignatureDesc.ppStaticSamplers = ppStaticSamplers;', 'avboitForwardRootSignatureDesc.ppStaticSamplers = staticSamplers;')
content = content.replace('avboitForwardRootSignatureDesc.ppStaticSamplerNames = pStaticSamplerNames;', 'avboitForwardRootSignatureDesc.ppStaticSamplerNames = staticSamplerNames;')
content = content.replace('avboitForwardRootSignatureDesc.mStaticSamplerCount = gStaticSamplerCount;', 'avboitForwardRootSignatureDesc.mStaticSamplerCount = numStaticSamplers;')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 54 applied.")
