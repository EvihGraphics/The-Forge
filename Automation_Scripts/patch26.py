import sys

file_path = 'Examples_3/Unit_Tests/src/15_Transparency/15_Transparency.cpp'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('            desc.mType = PIPELINE_TYPE_COMPUTE;\n            ComputePipelineDesc& avboitClearPipelineDesc = desc.mComputeDesc;', '            desc = {};\n            desc.mType = PIPELINE_TYPE_COMPUTE;\n            ComputePipelineDesc& avboitClearPipelineDesc = desc.mComputeDesc;')

content = content.replace('            desc.mType = PIPELINE_TYPE_GRAPHICS;\n            GraphicsPipelineDesc& avboitCompositePipelineDesc = desc.mGraphicsDesc;', '            desc = {};\n            desc.mType = PIPELINE_TYPE_GRAPHICS;\n            GraphicsPipelineDesc& avboitCompositePipelineDesc = desc.mGraphicsDesc;')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 26 applied.")
