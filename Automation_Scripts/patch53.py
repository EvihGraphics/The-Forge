import sys

file_path = 'Examples_3/Unit_Tests/src/15_Transparency/15_Transparency.cpp'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('avboitForwardRootSignatureDesc.mMaxBindlessTextures = gScene->numMaterials;', 'avboitForwardRootSignatureDesc.mMaxBindlessTextures = TEXTURE_COUNT;')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 53 applied.")
