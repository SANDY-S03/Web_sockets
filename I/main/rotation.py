import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('img2.jpg')

# Rotate clockwise by 90 degrees
rotated_clockwise = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

# Rotate anti-clockwise by 90 degrees
rotated_anticlockwise = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

# Display the original and rotated images using matplotlib
plt.figure(figsize=(10, 6))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(rotated_clockwise, cv2.COLOR_BGR2RGB))
plt.title('Rotated Clockwise by 90 degrees')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(rotated_anticlockwise, cv2.COLOR_BGR2RGB))
plt.title('Rotated Anti-clockwise by 90 degrees')
plt.axis('off')

plt.tight_layout()
plt.show()
