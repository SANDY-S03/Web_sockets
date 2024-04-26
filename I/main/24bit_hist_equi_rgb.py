import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the RGB image
image_path = '24bit_rgb.jpeg'  # Update with the actual path to your image
image = cv2.imread(image_path)

if image is None:
    print("Error: Image could not be loaded. Please check the file path.")
    exit()

# Convert the image to HSV color space
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Split the HSV image into channels
h, s, v = cv2.split(image_hsv)

# Equalize the Value (V) channel
v_eq = cv2.equalizeHist(v)

# Merge the equalized channels back into an HSV image
image_hsv_eq = cv2.merge([h, s, v_eq])

# Convert the equalized HSV image back to RGB
image_rgb_eq = cv2.cvtColor(image_hsv_eq, cv2.COLOR_HSV2BGR)

# Plot original and equalized image histograms
plt.figure(figsize=(10, 5))

# Original Image Histogram
plt.subplot(2, 2, 1)
plt.hist(image.ravel(), 256, [0, 256], color='b')
plt.title('Original Image Histogram')

# Equalized Image Histogram
plt.subplot(2, 2, 2)
plt.hist(image_rgb_eq.ravel(), 256, [0, 256], color='r')
plt.title('Equalized Image Histogram')

# Display the original and equalized images
plt.subplot(2, 2, 3)
plt.imshow(cv2.cvtColor(image_rgb_eq, cv2.COLOR_BGR2RGB))
plt.title('Equalized Image')
plt.axis('off')

plt.tight_layout()
plt.show()
