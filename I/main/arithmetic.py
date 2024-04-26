import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the input images
image1 = cv2.imread('img2.jpg')
image2 = cv2.imread('input_image2.jpg')

# Check if the images have the same dimensions
if image1.shape != image2.shape:
    print("Error: Input images must have the same dimensions.")
    exit()

# Convert the images to grayscale for arithmetic operations
image1_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
image2_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

# Perform addition of two grayscale images
image_add = cv2.add(image1_gray, image2_gray)

# Perform subtraction of two grayscale images
image_subtract = cv2.subtract(image1_gray, image2_gray)

# Display the original and processed images
plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title('Image 1')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title('Image 2')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(image_add, cmap='gray')
plt.title('Addition')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(image_subtract, cmap='gray')
plt.title('Subtraction')
plt.axis('off')

plt.tight_layout()
plt.show()
