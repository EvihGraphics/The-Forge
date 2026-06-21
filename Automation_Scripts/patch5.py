import sys
import re

file_path = 'Examples_3/Unit_Tests/src/15_Transparency/15_Transparency.cpp'
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

seen_globals = set()
global_patterns = [
    'pTextureAVBOITVolumeExtinction',
    'pTextureAVBOITVolumeTransmittanceLut',
    'pShaderAVBOITSplat',
    'pPipelineAVBOITSplat',
    'pRootSignatureAVBOITSplat',
    'pDescriptorSetAVBOITSplat',
    'pShaderAVBOITClear',
    'pPipelineAVBOITClear',
    'pRootSignatureAVBOITClear',
    'pDescriptorSetAVBOITClear',
    'pShaderAVBOITIntegrate',
    'pPipelineAVBOITIntegrate',
    'pRootSignatureAVBOITIntegrate',
    'pDescriptorSetAVBOITIntegrate',
    'pShaderAVBOITComposite',
    'pPipelineAVBOITComposite',
    'pRootSignatureAVBOITComposite',
    'pDescriptorSetAVBOITComposite',
    'pBufferAVBOITUniform'
]

new_lines = []

for line_idx, line in enumerate(lines):
    # Fix setDesc issues
    if 'setDesc = { pRootSignatureAVBOIT' in line:
        parts = line.split('{')[1].split('}')[0].split(',')
        if len(parts) >= 3:
            rs = parts[0].strip()
            freq = parts[1].strip()
            cnt = parts[2].strip()
            spaces = line[:len(line) - len(line.lstrip())]
            line = f"{spaces}setDesc.pRootSignature = {rs}; setDesc.mUpdateFrequency = {freq}; setDesc.mMaxSets = {cnt};\n"

    # Remove duplicate globals
    is_global_decl = False
    if '= NULL' in line or '= { NULL }' in line:
        for p in global_patterns:
            if re.search(r'\b' + p + r'\b', line) and ('Texture*' in line or 'Shader*' in line or 'Pipeline*' in line or 'RootSignature*' in line or 'DescriptorSet*' in line or 'Buffer*' in line):
                is_global_decl = True
                if p in seen_globals:
                    line = "" # Delete it
                else:
                    seen_globals.add(p)
                break
    
    # Also clean up empty AVBOIT Shaders comments if we deleted the line
    if line.strip() == '// AVBOIT Shaders':
        # Let's just keep it, doesn't break compile
        pass

    if line != "":
        new_lines.append(line)

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Patch 5 applied.")
