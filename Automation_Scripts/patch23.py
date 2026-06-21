import sys
import re

file_path = 'Examples_3/Unit_Tests/src/15_Transparency/15_Transparency.cpp'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('pTextureAVBOITVolumeExtinction', 'pBufferAVBOITVolumeExtinction')
content = content.replace('pTextureAVBOITVolumeColor', 'pBufferAVBOITVolumeColor')

content = content.replace('ppTextures = &pBufferAVBOITVolumeExtinction', 'ppBuffers = &pBufferAVBOITVolumeExtinction')
content = content.replace('ppTextures = &pBufferAVBOITVolumeColor', 'ppBuffers = &pBufferAVBOITVolumeColor')
content = content.replace('ppTexture = &pBufferAVBOITVolumeExtinction', 'ppBuffer = &pBufferAVBOITVolumeExtinction')
content = content.replace('ppTexture = &pBufferAVBOITVolumeColor', 'ppBuffer = &pBufferAVBOITVolumeColor')

# Also fix any remaining barriers that might be using TextureBarrier struct with pBuffer pointer
content = re.sub(r'TextureBarrier\s+(\w+)\s*=\s*\{\s*pBufferAVBOITVolumeExtinction', r'BufferBarrier \1 = { pBufferAVBOITVolumeExtinction', content)
content = re.sub(r'TextureBarrier\s+(\w+)\s*=\s*\{\s*pBufferAVBOITVolumeColor', r'BufferBarrier \1 = { pBufferAVBOITVolumeColor', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 23 applied.")
