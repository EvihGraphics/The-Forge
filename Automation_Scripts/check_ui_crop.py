from PIL import Image
import numpy as np

img = Image.open('C:/Users/l3d/.gemini/antigravity/brain/2d7a8410-35e6-47b7-a5c1-e3ce6a91a404/Mode_6_UI_Crop.png').convert('RGB')
arr = np.array(img)
print(f"Mean RGB: {arr.mean(axis=(0,1))}")
print(f"Standard Deviation RGB: {arr.std(axis=(0,1))}")
