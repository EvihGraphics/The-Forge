import sys

file_path = 'Examples_3/Unit_Tests/src/15_Transparency/15_Transparency.cpp'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('LOGF(eINFO, "Adding AVBOITSplat Pipeline...");', 'LOGF(eINFO, "Adding AVBOITSplat Pipeline... pShaderAVBOITSplat=%p", pShaderAVBOITSplat);')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 34 applied.")
