from PIL import Image
import numpy as np

img = Image.open(r'C:\Users\l3d\.gemini\antigravity\brain\2d7a8410-35e6-47b7-a5c1-e3ce6a91a404\AVBOIT_Fixed_Screen.png').convert('RGB')
arr = np.array(img)
print(f"Max RGB: {arr.max(axis=(0,1))}")
print(f"Mean RGB: {arr.mean(axis=(0,1))}")
