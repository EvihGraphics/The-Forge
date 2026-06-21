import numpy as np
from PIL import Image

def mse(imageA, imageB):
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1] * imageA.shape[2])
    return err

img_avboit = Image.open(r'C:\Users\l3d\.gemini\antigravity\brain\2d7a8410-35e6-47b7-a5c1-e3ce6a91a404\AVBOIT_Fixed_Screen_Cropped.png').convert('RGB')
img_gt = Image.open(r'C:\Users\l3d\.gemini\antigravity\brain\2d7a8410-35e6-47b7-a5c1-e3ce6a91a404\GroundTruth_Mode_0.png').convert('RGB')

# Ensure sizes match
if img_avboit.size != img_gt.size:
    img_gt = img_gt.resize(img_avboit.size)

arr_avboit = np.array(img_avboit)
arr_gt = np.array(img_gt)

error = mse(arr_avboit, arr_gt)
print(f"MSE between Fixed AVBOIT (Cropped) and Ground Truth: {error}")
