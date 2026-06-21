import sys

file_path = 'Examples_3/Unit_Tests/src/15_Transparency/15_Transparency.cpp'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('addPipeline(pRenderer, &desc, &pPipelineAVBOITSplat);', 'LOGF(eINFO, "Adding AVBOITSplat Pipeline...");\n            addPipeline(pRenderer, &desc, &pPipelineAVBOITSplat);')
content = content.replace('addPipeline(pRenderer, &desc, &pPipelineAVBOITClear);', 'LOGF(eINFO, "Adding AVBOITClear Pipeline...");\n            addPipeline(pRenderer, &desc, &pPipelineAVBOITClear);')
content = content.replace('addPipeline(pRenderer, &desc, &pPipelineAVBOITIntegrate);', 'LOGF(eINFO, "Adding AVBOITIntegrate Pipeline...");\n            addPipeline(pRenderer, &desc, &pPipelineAVBOITIntegrate);')
content = content.replace('addPipeline(pRenderer, &desc, &pPipelineAVBOITComposite);', 'LOGF(eINFO, "Adding AVBOITComposite Pipeline...");\n            addPipeline(pRenderer, &desc, &pPipelineAVBOITComposite);')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 29 applied.")
