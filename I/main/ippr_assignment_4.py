import cv2
import numpy as np
from matplotlib import pyplot as plt

def histogram_equalization(image):
    # Convert the image to grayscale if it's in color
    if len(image.shape) > 2:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray_image = image
    
    # Perform histogram equalization
    equalized_image = cv2.equalizeHist(gray_image)
    
    return equalized_image

# Read the image
img = cv2.imread('img2.jpg')

# Display the original image and its histogram
plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original Image')

plt.subplot(2, 2, 2)
plt.hist(img.ravel(), 256, [0, 256])
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.title('Histogram of Original Image')

# Perform histogram equalization
equ = histogram_equalization(img)

# Display the equalized image and its histogram
plt.subplot(2, 2, 3)
plt.imshow(equ, cmap='gray')
plt.title('Equalized Image')

plt.subplot(2, 2, 4)
plt.hist(equ.ravel(), 256, [0, 256])
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.title('Histogram of Equalized Image')

plt.tight_layout()
plt.show()

# Save the equalized image
cv2.imwrite('equalized_image.jpg', equ)