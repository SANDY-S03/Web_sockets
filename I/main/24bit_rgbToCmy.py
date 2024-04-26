import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the RGB image
image_path = '24bit_rgb.jpeg'  # Update the path to your image
image = cv2.imread(image_path)

# Check if the image has been loaded properly
if image is None:
    print("Error: Image could not be read.")
    exit()

# Convert RGB to CMY
# Subtracting RGB colors from 255
cmy_image = 255 - image

# Display the original and CMY images using matplotlib
plt.figure(figsize=(12, 6))

# Display original image
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original RGB Image')
plt.axis('off')

# Display CMY image - Note: Displaying it as RGB since it's visually similar
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(cmy_image, cv2.COLOR_BGR2RGB))
plt.title('CMY Image ')
plt.axis('off')

plt.tight_layout()
plt.show()
