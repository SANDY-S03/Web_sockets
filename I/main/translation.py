import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('img2.jpg')

# Define the translation amounts
shift_right = 50
shift_down = 100

# Construct the translation matrices
M_right = np.float32([[1, 0, shift_right], [0, 1, 0]])  # Shift right by 20 units
M_down = np.float32([[1, 0, 0], [0, 1, shift_down]])  # Shift down by 10 units

# Perform translation
translated_image_right = cv2.warpAffine(image, M_right, (image.shape[1], image.shape[0]))
translated_image_down = cv2.warpAffine(image, M_down, (image.shape[1], image.shape[0]))

# Display the original and translated images using matplotlib
plt.figure(figsize=(10, 6))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(translated_image_right, cv2.COLOR_BGR2RGB))
plt.title('Shifted Right by 20 units')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(translated_image_down, cv2.COLOR_BGR2RGB))
plt.title('Shifted Downwards by 10 units')
plt.axis('off')

plt.tight_layout()
plt.show()
