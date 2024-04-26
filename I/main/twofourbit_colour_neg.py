import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the color image
image = cv2.imread('24bit_colour.jpeg')

# Check if the image has been loaded properly
if image is None:
    print("Error: Image could not be read.")
    exit()

# Calculate the negative image by subtracting image data from 255
negative_image = 255 - image

# Display the original and negative images using matplotlib
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(negative_image, cv2.COLOR_BGR2RGB))
plt.title('Negative Image')
plt.axis('off')

plt.tight_layout()
plt.show()
