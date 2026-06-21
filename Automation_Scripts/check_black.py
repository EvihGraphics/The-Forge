from PIL import Image
import numpy as np

img = Image.open(r'D:\Users\l3d\Documents\AVBOIT\The-Forge\LocalVisualResults\HIVE_4090x2\VisualResults\Screenshots\UT_15_Transparency_DX12_Mode_5_AVBOIT.png').convert('RGB')
arr = np.array(img)
print(f"Max RGB: {arr.max(axis=(0,1))}")
print(f"Mean RGB: {arr.mean(axis=(0,1))}")
