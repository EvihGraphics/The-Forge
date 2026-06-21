from PIL import Image
import numpy as np

img0 = Image.open('LocalVisualResults/HIVE_4090x2/VisualResults/15_Transparency/Screenshots/UT_15_Transparency_DX12_Mode_0.png').convert('RGB')
img6 = Image.open('LocalVisualResults/HIVE_4090x2/VisualResults/15_Transparency/Screenshots/UT_15_Transparency_DX12_Mode_6.png').convert('RGB')

if img0.size != img6.size:
    # Resize img6 to match img0 for comparison if sizes differ slightly due to window capture
    img6 = img6.resize(img0.size)

arr0 = np.array(img0).astype(float)
arr6 = np.array(img6).astype(float)

mse = np.mean((arr0 - arr6) ** 2)
print(f"MSE between Mode 0 and Mode 6: {mse:.4f}")
