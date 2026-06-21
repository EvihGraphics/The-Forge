import os
path = r'D:\Users\l3d\Documents\AVBOIT\The-Forge\Examples_3\Unit_Tests\src\15_Transparency\15_Transparency.cpp'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'GuiController::RemoveGui();' in line:
        lines.insert(i + 1, '        LOGF(LogLevel::eINFO, "OIT Performance Dump [Mode %u]: %f ms", gTransparencyType, getGpuProfileAvgTime(gCurrentGpuProfileTokens[gTransparencyType]));\n')
        break

with open(path, 'w', encoding='utf-8') as f:
    f.writelines(lines)
