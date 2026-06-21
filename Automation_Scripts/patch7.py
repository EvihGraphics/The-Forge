import codecs

file_path = 'Examples_3/Unit_Tests/src/15_Transparency/Shaders/FSL/ShaderList.fsl'
with open(file_path, 'rb') as f:
    content = f.read()

# remove BOM if present
if content.startswith(codecs.BOM_UTF8):
    content = content[len(codecs.BOM_UTF8):]

# write back without BOM
with open(file_path, 'wb') as f:
    f.write(content)

cpp_path = 'Examples_3/Unit_Tests/src/15_Transparency/15_Transparency.cpp'
with open(cpp_path, 'r', encoding='utf-8') as f:
    cpp_content = f.read()

# Fix desc redefinition
cpp_content = cpp_content.replace('PipelineDesc desc = {};', 'PipelineDesc avboitDesc = {};')
cpp_content = cpp_content.replace('desc.mType = PIPELINE_TYPE_', 'avboitDesc.mType = PIPELINE_TYPE_')
cpp_content = cpp_content.replace('desc.mGraphicsDesc;', 'avboitDesc.mGraphicsDesc;')
cpp_content = cpp_content.replace('desc.mComputeDesc;', 'avboitDesc.mComputeDesc;')
cpp_content = cpp_content.replace('addPipeline(pRenderer, &desc, &pPipelineAVBOITSplat);', 'addPipeline(pRenderer, &avboitDesc, &pPipelineAVBOITSplat);')
cpp_content = cpp_content.replace('addPipeline(pRenderer, &desc, &pPipelineAVBOITClear);', 'addPipeline(pRenderer, &avboitDesc, &pPipelineAVBOITClear);')
cpp_content = cpp_content.replace('addPipeline(pRenderer, &desc, &pPipelineAVBOITIntegrate);', 'addPipeline(pRenderer, &avboitDesc, &pPipelineAVBOITIntegrate);')
cpp_content = cpp_content.replace('addPipeline(pRenderer, &desc, &pPipelineAVBOITComposite);', 'addPipeline(pRenderer, &avboitDesc, &pPipelineAVBOITComposite);')

with open(cpp_path, 'w', encoding='utf-8') as f:
    f.write(cpp_content)

print("Patch 7 applied.")
