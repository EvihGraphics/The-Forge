from PIL import Image
img = Image.open(r'D:\Users\l3d\Documents\AVBOIT\The-Forge\LocalVisualResults\HIVE_4090x2\VisualResults\Screenshots\UT_15_Transparency_DX12_Mode_5_AVBOIT.png')
# UI is usually on the top left or top right
# Let's crop the top left 600x400
cropped = img.crop((0, 0, 600, 400))
cropped.save(r'C:\Users\l3d\.gemini\antigravity\brain\2d7a8410-35e6-47b7-a5c1-e3ce6a91a404\Mode_5_UI_Crop.png')
