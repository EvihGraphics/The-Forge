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

inject(r'addDescriptorSet\(pRenderer, &aoitClearDescriptorSetDesc, &pDescriptorSetAOITClear\);', '''
        // AVBOIT Descriptor Sets
        {
            DescriptorSetDesc setDesc = { pRootSignatureAVBOITSplat, DESCRIPTOR_UPDATE_FREQ_NONE, 1 };
            addDescriptorSet(pRenderer, &setDesc, &pDescriptorSetAVBOITSplat[0]);
            setDesc = { pRootSignatureAVBOITSplat, DESCRIPTOR_UPDATE_FREQ_PER_FRAME, gDataBufferCount };
            addDescriptorSet(pRenderer, &setDesc, &pDescriptorSetAVBOITSplat[1]);

            setDesc = { pRootSignatureAVBOITClear, DESCRIPTOR_UPDATE_FREQ_PER_FRAME, 1 };
            addDescriptorSet(pRenderer, &setDesc, &pDescriptorSetAVBOITClear);

            setDesc = { pRootSignatureAVBOITIntegrate, DESCRIPTOR_UPDATE_FREQ_PER_FRAME, 1 };
            addDescriptorSet(pRenderer, &setDesc, &pDescriptorSetAVBOITIntegrate);

            setDesc = { pRootSignatureAVBOITComposite, DESCRIPTOR_UPDATE_FREQ_PER_FRAME, 1 };
            addDescriptorSet(pRenderer, &setDesc, &pDescriptorSetAVBOITComposite);
        }
''')

inject(r'removeDescriptorSet\(pRenderer, pDescriptorSetAOITClear\);', '''
        removeDescriptorSet(pRenderer, pDescriptorSetAVBOITSplat[0]);
        removeDescriptorSet(pRenderer, pDescriptorSetAVBOITSplat[1]);
        removeDescriptorSet(pRenderer, pDescriptorSetAVBOITClear);
        removeDescriptorSet(pRenderer, pDescriptorSetAVBOITIntegrate);
        removeDescriptorSet(pRenderer, pDescriptorSetAVBOITComposite);
''')

inject(r'updateDescriptorSet\(pRenderer, 0, pDescriptorSetAOITComposite, 2, compositeParams\);', '''
        // AVBOIT update descriptors
        {
            DescriptorData clearParams[2] = {};
            clearParams[0].pName = "VolumeExtinctionBufferUAV";
            clearParams[0].ppTextures = &pTextureAVBOITVolumeExtinction;
            clearParams[1].pName = "VolumeTransmittanceLutUAV";
            clearParams[1].ppTextures = &pTextureAVBOITVolumeTransmittanceLut;
            updateDescriptorSet(pRenderer, 0, pDescriptorSetAVBOITClear, 2, clearParams);

            DescriptorData integrateParams[2] = {};
            integrateParams[0].pName = "VolumeExtinctionBufferSRV";
            integrateParams[0].ppTextures = &pTextureAVBOITVolumeExtinction;
            integrateParams[1].pName = "VolumeTransmittanceLutUAV";
            integrateParams[1].ppTextures = &pTextureAVBOITVolumeTransmittanceLut;
            updateDescriptorSet(pRenderer, 0, pDescriptorSetAVBOITIntegrate, 2, integrateParams);

            DescriptorData compositeParams[1] = {};
            compositeParams[0].pName = "VolumeTransmittanceLutSRV";
            compositeParams[0].ppTextures = &pTextureAVBOITVolumeTransmittanceLut;
            updateDescriptorSet(pRenderer, 0, pDescriptorSetAVBOITComposite, 1, compositeParams);

            DescriptorData splatParams[1] = {};
            splatParams[0].pName = "VolumeExtinctionBufferUAV";
            splatParams[0].ppTextures = &pTextureAVBOITVolumeExtinction;
            updateDescriptorSet(pRenderer, 0, pDescriptorSetAVBOITSplat[0], 1, splatParams);

            for (uint32_t i = 0; i < gDataBufferCount; ++i)
            {
                DescriptorData splatFrameParams[2] = {};
                splatFrameParams[0].pName = "cameraUniformBlock";
                splatFrameParams[0].ppBuffers = &pBufferCameraUniform[i];
                splatFrameParams[1].pName = "AVBOITUniforms";
                splatFrameParams[1].ppBuffers = &pBufferAVBOITUniform[i];
                updateDescriptorSet(pRenderer, i, pDescriptorSetAVBOITSplat[1], 2, splatFrameParams);
            }
        }
''')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Injection Phase 5 complete.")
