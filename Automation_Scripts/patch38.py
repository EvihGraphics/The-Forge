import sys

file_path = 'Examples_3/Unit_Tests/src/15_Transparency/Shaders/FSL/AVBOIT.frag.fsl'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('#include "shaderDefs.h.fsl"\n\n', '''STRUCT(VSOutput)
{
	DATA(float4, Position, SV_Position);
	DATA(float4, WorldPosition, POSITION);
	DATA(float4, Normal, NORMAL);
	DATA(float4, UV, TEXCOORD0);
	DATA(FLAT(uint), MatID, MAT_ID);
#if FT_MULTIVIEW
	DATA(FLAT(uint), ViewID, TEXCOORD1);
#endif
};

''')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 38 applied.")
