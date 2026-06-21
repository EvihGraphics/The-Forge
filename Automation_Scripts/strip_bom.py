import codecs
import glob
import os

for file_path in glob.glob('Examples_3/Unit_Tests/src/15_Transparency/Shaders/FSL/*.fsl'):
    with open(file_path, 'rb') as f:
        content = f.read()

    if content.startswith(codecs.BOM_UTF8):
        content = content[len(codecs.BOM_UTF8):]
        with open(file_path, 'wb') as f:
            f.write(content)
        print(f"Removed BOM from {os.path.basename(file_path)}")
