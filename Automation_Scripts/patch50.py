import sys

file_path = 'Examples_3/Unit_Tests/src/15_Transparency/15_Transparency.cpp'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('avboitForwardShaderDesc.mStages[0] = { "skybox.vert", NULL, 0, NULL, SHADER_STAGE_LOAD_FLAG_ENABLE_VR_MULTIVIEW };', 'avboitForwardShaderDesc.mStages[0] = { "forward.vert" };')
content = content.replace('avboitForwardShaderDesc.mStages[1] = { "avboit_forward.frag", NULL, 0, NULL, SHADER_STAGE_LOAD_FLAG_ENABLE_VR_MULTIVIEW };', 'avboitForwardShaderDesc.mStages[1] = { "avboit_forward.frag" };')
content = content.replace('avboitForwardPipelineDesc.pVertexLayout = &vertexLayout;', 'avboitForwardPipelineDesc.pVertexLayout = &vertexLayoutDefault;')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 50 applied.")
