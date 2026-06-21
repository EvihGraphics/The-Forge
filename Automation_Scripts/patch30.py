import sys

file_path = 'Examples_3/Unit_Tests/src/15_Transparency/15_Transparency.cpp'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('''                DescriptorData avboitSplatFrameParams[2] = {};
                avboitSplatFrameParams[0].pName = "cameraUniformBlock";
                avboitSplatFrameParams[0].ppBuffers = &pBufferCameraUniform[i];
                avboitSplatFrameParams[1].pName = "AVBOITUniforms";
                avboitSplatFrameParams[1].ppBuffers = &pBufferAVBOITUniform[i];
                updateDescriptorSet(pRenderer, i, pDescriptorSetAVBOITSplat[1], 2, avboitSplatFrameParams);''',
'''                DescriptorData avboitSplatFrameParams[1] = {};
                avboitSplatFrameParams[0].pName = "AVBOITUniforms";
                avboitSplatFrameParams[0].ppBuffers = &pBufferAVBOITUniform[i];
                updateDescriptorSet(pRenderer, i, pDescriptorSetAVBOITSplat[1], 1, avboitSplatFrameParams);''')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 30 applied.")
