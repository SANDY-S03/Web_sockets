#Image Normalization
import cv2
import numpy as np
import matplotlib.pyplot as plt


# Read the uploaded image
image_path = 'img2.jpg'
img = cv2.imread(image_path)

# Convert the image from BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Display the original image
plt.figure(figsize=(6, 6))
plt.subplot(1, 2, 1)
plt.imshow(img_rgb)
plt.title('Original Image')

# Normalize the image to the range [0, 1]
normalized_img = img_rgb / 255.0

# Display the normalized image
plt.subplot(1, 2, 2)
plt.imshow(normalized_img)
plt.title('Normalized Image')

plt.show()