import sys

file_path = 'Examples_3/Unit_Tests/src/15_Transparency/15_Transparency.cpp'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('avboitExtLoadDesc.mDesc.mElementCount = 1920 * 1080 * 64;', 'avboitExtLoadDesc.mDesc.mElementCount = mSettings.mWidth * mSettings.mHeight * 64;')
content = content.replace('avboitTransmittanceDesc.mWidth = 1920;', 'avboitTransmittanceDesc.mWidth = mSettings.mWidth;')
content = content.replace('avboitTransmittanceDesc.mHeight = 1080;', 'avboitTransmittanceDesc.mHeight = mSettings.mHeight;')

# In Draw(), the uniform array needs to be updated. Let's find: uint32_t avboitUniformData[4] = { 1920, 1080, 64, 0 };
content = content.replace('uint32_t avboitUniformData[4] = { 1920, 1080, 64, 0 };', 'uint32_t avboitUniformData[4] = { (uint32_t)mSettings.mWidth, (uint32_t)mSettings.mHeight, 64, 0 };')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch 44 applied.")
