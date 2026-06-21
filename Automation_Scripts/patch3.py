import re

file_path = 'Examples_3/Unit_Tests/src/15_Transparency/15_Transparency.cpp'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Clean up duplicate global blocks
# Find all occurrences of the block and keep only the first one
global_block_regex = r'// AVBOIT Shaders\s+Shader\* pShaderAVBOITSplat = NULL;\s+Shader\* pShaderAVBOITClear = NULL;\s+Shader\* pShaderAVBOITIntegrate = NULL;\s+Shader\* pShaderAVBOITComposite = NULL;\s+RootSignature\* pRootSignatureAVBOITSplat = NULL;\s+RootSignature\* pRootSignatureAVBOITClear = NULL;\s+RootSignature\* pRootSignatureAVBOITIntegrate = NULL;\s+RootSignature\* pRootSignatureAVBOITComposite = NULL;\s+Pipeline\* pPipelineAVBOITSplat = NULL;\s+Pipeline\* pPipelineAVBOITClear = NULL;\s+Pipeline\* pPipelineAVBOITIntegrate = NULL;\s+Pipeline\* pPipelineAVBOITComposite = NULL;\s+Texture\* pTextureAVBOITVolumeExtinction = NULL;\s+Texture\* pTextureAVBOITVolumeTransmittanceLut = NULL;\s+DescriptorSet\* pDescriptorSetAVBOITSplat\[2\] = \{ NULL \};\s+DescriptorSet\* pDescriptorSetAVBOITClear = NULL;\s+DescriptorSet\* pDescriptorSetAVBOITIntegrate = NULL;\s+DescriptorSet\* pDescriptorSetAVBOITComposite = NULL;'

matches = list(re.finditer(global_block_regex, content))
if len(matches) > 1:
    # Keep the first, remove the rest
    for match in reversed(matches[1:]):
        content = content[:match.start()] + content[match.end():]
        print("Removed duplicate global block")

# 2. Fix setDesc = { ... }
# Let's use regex to find and replace them all safely
content = re.sub(
    r'setDesc = \{\s*([a-zA-Z0-9_]+),\s*([a-zA-Z0-9_]+),\s*([a-zA-Z0-9_]+)\s*\};',
    r'setDesc = {}; setDesc.pRootSignature = \1; setDesc.mUpdateFrequency = \2; setDesc.mMaxSets = \3;',
    content
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 3 applied.")
