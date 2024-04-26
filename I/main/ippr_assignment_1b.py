import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img = Image.open("ippr_assignment_1a_img1.jpg")
M = np.asarray(img)

red_channel = M[:, :, 0]
green_channel = M[:, :, 1]
blue_channel = M[:, :, 2]

red_enhanced = np.clip(red_channel * 1.5, 0, 255)
green_enhanced = np.clip(green_channel * 1.5, 0, 255)
blue_enhanced = np.clip(blue_channel * 1.5, 0, 255)

# Create enhanced images for each channel
red_enhanced_image = np.stack((red_enhanced, np.zeros_like(green_channel), np.zeros_like(blue_channel)), axis=-1).astype(np.uint8)
green_enhanced_image = np.stack((np.zeros_like(red_channel), green_enhanced, np.zeros_like(blue_channel)), axis=-1).astype(np.uint8)
blue_enhanced_image = np.stack((np.zeros_like(red_channel), np.zeros_like(green_channel), blue_enhanced), axis=-1).astype(np.uint8)

# Convert enhanced images to PIL Image
red_enhanced_image = Image.fromarray(red_enhanced_image)
green_enhanced_image = Image.fromarray(green_enhanced_image)
blue_enhanced_image = Image.fromarray(blue_enhanced_image)

plt.figure(figsize=(12, 12))

plt.subplot(2, 2, 1)
plt.imshow(img)
plt.title("Original Image")

plt.subplot(2, 2, 2)
plt.imshow(red_enhanced_image)
plt.title("Enhanced Image (Red Channel)")

plt.subplot(2, 2, 3)
plt.imshow(green_enhanced_image)
plt.title("Enhanced Image (Green Channel)")

plt.subplot(2, 2, 4)
plt.imshow(blue_enhanced_image)
plt.title("Enhanced Image (Blue Channel)")

plt.show()