import sys

file_path = 'Examples_3/Unit_Tests/src/15_Transparency/15_Transparency.cpp'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('avboitForwardRootSignatureDesc.ppStaticSamplers = ppStaticSamplers;', 'avboitForwardRootSignatureDesc.ppStaticSamplers = ppStaticSamplers;\n            avboitForwardRootSignatureDesc.ppStaticSamplerNames = pStaticSamplerNames;')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 51 applied.")
