import re
import sys

file_path = 'Examples_3/Unit_Tests/src/15_Transparency/15_Transparency.cpp'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

def inject(pattern, new_code):
    global content
    matches = list(re.finditer(pattern, content, re.MULTILINE))
    if not matches:
        print(f"Failed to find pattern: {pattern}")
        sys.exit(1)
    match = matches[-1]
    content = content[:match.end()] + "\n" + new_code + content[match.end():]
    print(f"Injected successfully after {pattern.strip()[:30]}")

inject(r'addDescriptorSet\(pRenderer, &setDesc, &pDescriptorSetAOITClear\);', '''
            // AVBOIT Descriptor Sets
            setDesc = { pRootSignatureAVBOITSplat, DESCRIPTOR_UPDATE_FREQ_NONE, 1 };
            addDescriptorSet(pRenderer, &setDesc, &pDescriptorSetAVBOITSplat[0]);
            setDesc = { pRootSignatureAVBOITSplat, DESCRIPTOR_UPDATE_FREQ_PER_FRAME, gDataBufferCount };
            addDescriptorSet(pRenderer, &setDesc, &pDescriptorSetAVBOITSplat[1]);

            setDesc = { pRootSignatureAVBOITClear, DESCRIPTOR_UPDATE_FREQ_NONE, 1 };
            addDescriptorSet(pRenderer, &setDesc, &pDescriptorSetAVBOITClear);

            setDesc = { pRootSignatureAVBOITIntegrate, DESCRIPTOR_UPDATE_FREQ_NONE, 1 };
            addDescriptorSet(pRenderer, &setDesc, &pDescriptorSetAVBOITIntegrate);

            setDesc = { pRootSignatureAVBOITComposite, DESCRIPTOR_UPDATE_FREQ_NONE, 1 };
            addDescriptorSet(pRenderer, &setDesc, &pDescriptorSetAVBOITComposite);
''')

inject(r'removeDescriptorSet\(pRenderer, pDescriptorSetAOITClear\);', '''
            removeDescriptorSet(pRenderer, pDescriptorSetAVBOITSplat[0]);
            removeDescriptorSet(pRenderer, pDescriptorSetAVBOITSplat[1]);
            removeDescriptorSet(pRenderer, pDescriptorSetAVBOITClear);
            removeDescriptorSet(pRenderer, pDescriptorSetAVBOITIntegrate);
            removeDescriptorSet(pRenderer, pDescriptorSetAVBOITComposite);
''')

inject(r'updateDescriptorSet\(pRenderer, 0, pDescriptorSetAOITClear, 1, clearParams\);', '''
            DescriptorData avboitClearParams[2] = {};
            avboitClearParams[0].pName = "VolumeExtinctionBufferUAV";
            avboitClearParams[0].ppTextures = &pTextureAVBOITVolumeExtinction;
            avboitClearParams[1].pName = "VolumeTransmittanceLutUAV";
            avboitClearParams[1].ppTextures = &pTextureAVBOITVolumeTransmittanceLut;
            updateDescriptorSet(pRenderer, 0, pDescriptorSetAVBOITClear, 2, avboitClearParams);

            DescriptorData avboitIntegrateParams[2] = {};
            avboitIntegrateParams[0].pName = "VolumeExtinctionBufferSRV";
            avboitIntegrateParams[0].ppTextures = &pTextureAVBOITVolumeExtinction;
            avboitIntegrateParams[1].pName = "VolumeTransmittanceLutUAV";
            avboitIntegrateParams[1].ppTextures = &pTextureAVBOITVolumeTransmittanceLut;
            updateDescriptorSet(pRenderer, 0, pDescriptorSetAVBOITIntegrate, 2, avboitIntegrateParams);

            DescriptorData avboitCompositeParams[1] = {};
            avboitCompositeParams[0].pName = "VolumeTransmittanceLutSRV";
            avboitCompositeParams[0].ppTextures = &pTextureAVBOITVolumeTransmittanceLut;
            updateDescriptorSet(pRenderer, 0, pDescriptorSetAVBOITComposite, 1, avboitCompositeParams);

            DescriptorData avboitSplatParams[1] = {};
            avboitSplatParams[0].pName = "VolumeExtinctionBufferUAV";
            avboitSplatParams[0].ppTextures = &pTextureAVBOITVolumeExtinction;
            updateDescriptorSet(pRenderer, 0, pDescriptorSetAVBOITSplat[0], 1, avboitSplatParams);

            for (uint32_t i = 0; i < gDataBufferCount; ++i)
            {
                DescriptorData avboitSplatFrameParams[2] = {};
                avboitSplatFrameParams[0].pName = "cameraUniformBlock";
                avboitSplatFrameParams[0].ppBuffers = &pBufferCameraUniform[i];
                avboitSplatFrameParams[1].pName = "AVBOITUniforms";
                avboitSplatFrameParams[1].ppBuffers = &pBufferAVBOITUniform[i];
                updateDescriptorSet(pRenderer, i, pDescriptorSetAVBOITSplat[1], 2, avboitSplatFrameParams);
            }
''')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Injection Phase 5 complete.")
