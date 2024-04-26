import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the input image
image = cv2.imread('img2.jpg')

# Convert the image to grayscale
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Set the threshold value (adjust as needed)
threshold_value = 64

# Apply thresholding
_, binary_image = cv2.threshold(image_gray, threshold_value, 255, cv2.THRESH_BINARY)

# Display the original and binary images
plt.figure(figsize=(10, 6))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(binary_image, cmap='binary')
plt.title('Binary Image (Threshold = {})'.format(threshold_value))
plt.axis('off')

plt.tight_layout()
plt.show()
