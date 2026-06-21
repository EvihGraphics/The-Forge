from PIL import Image
import numpy as np

img0 = Image.open(r'C:\Users\l3d\.gemini\antigravity\brain\2d7a8410-35e6-47b7-a5c1-e3ce6a91a404\FullScreenCapture.png').convert('RGB')
img6 = Image.open(r'C:\Users\l3d\.gemini\antigravity\brain\2d7a8410-35e6-47b7-a5c1-e3ce6a91a404\FullScreen_AVBOIT.png').convert('RGB')

arr0 = np.array(img0).astype(float)
arr6 = np.array(img6).astype(float)

mse = np.mean((arr0 - arr6) ** 2)
print(f"MSE between FullScreen Mode 0 and Mode 6: {mse:.4f}")
