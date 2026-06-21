import sys

file_path = 'Examples_3/Unit_Tests/src/15_Transparency/15_Transparency.cpp'
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
in_globals = False
global_decls_count = 0

for idx, line in enumerate(lines):
    # Fix setDesc issues
    if 'setDesc = { pRootSignatureAVBOIT' in line:
        parts = line.split('{')[1].split('}')[0].split(',')
        if len(parts) == 3:
            rs = parts[0].strip()
            freq = parts[1].strip()
            cnt = parts[2].strip()
            spaces = line[:len(line) - len(line.lstrip())]
            line = f"{spaces}setDesc = {{}}; setDesc.pRootSignature = {rs}; setDesc.mUpdateFrequency = {freq}; setDesc.mMaxSets = {cnt};\n"
    
    # Remove duplicate globals (we only want the very first one we encounter)
    if '// AVBOIT Shaders' in line:
        global_decls_count += 1
        if global_decls_count > 1:
            in_globals = True
            continue
    
    if in_globals:
        if 'DescriptorSet* pDescriptorSetAVBOITComposite' in line:
            in_globals = False # End of block
        continue
    
    new_lines.append(line)

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Patch 4 applied.")
