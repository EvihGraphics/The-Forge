import sys

file_path = 'Examples_3/Unit_Tests/src/15_Transparency/Shaders/FSL/AVBOIT.frag.fsl'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('#include "shaderDefs.h.fsl"\n\n', '#include "shaderDefs.h.fsl"\n#include "shading.h.fsl"\n\n')

content = content.replace('''void PS_MAIN( VSOutput In )
{
    INIT_MAIN;
    float4 color = In.Color;
    // (Omitted: shading calculations for simplicity, assuming simple transparent quads)
    
    DrawTransparent(In.Position, color);
    
    clip(-1.0f);
    RETURN();
}''', '''EARLY_FRAGMENT_TESTS
void PS_MAIN( VSOutput In )
{
    INIT_MAIN;
    float4 finalColor = Shade(In.MatID, In.UV.xy, In.WorldPosition.xyz, normalize(In.Normal.xyz), VR_VIEW_ID(In.ViewID));
    
    if (finalColor.a > 0.01f)
    {
        DrawTransparent(In.Position, finalColor);
    }
    
    clip(-1.0f);
    RETURN();
}''')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 39 applied.")
