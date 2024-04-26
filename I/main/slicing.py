import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the input image
image = cv2.imread('img2.jpg')

# Convert the image to grayscale
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Define the intensity range to highlight (adjust as needed)
low_intensity = 50
high_intensity = 200

# Create a mask for preserving the background
mask_preserve = cv2.inRange(image_gray, low_intensity, high_intensity)

# Apply the mask to the original image
output_preserve = cv2.bitwise_and(image, image, mask=mask_preserve)

# Create a mask for non-preserving the background
mask_non_preserve = cv2.bitwise_not(mask_preserve)

# Create a white background image
white_background = np.full_like(image, (255, 255, 255))

# Apply the mask to the white background image
output_non_preserve = cv2.bitwise_and(white_background, white_background, mask=mask_non_preserve)

# Combine the preserved and non-preserved parts
output_combined = cv2.bitwise_or(output_preserve, output_non_preserve)

# Display the original image and processed images
plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(output_preserve, cv2.COLOR_BGR2RGB))
plt.title('With Preserving Background')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(output_combined, cv2.COLOR_BGR2RGB))
plt.title('Non-preserving Background')
plt.axis('off')

plt.tight_layout()
plt.show()
