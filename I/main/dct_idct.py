import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('img2.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply DCT (Discrete Cosine Transform)
dct_image = cv2.dct(np.float32(gray_image))

# Apply inverse DCT (IDCT) to retrieve the image
idct_image = cv2.idct(dct_image)

# Convert back to uint8 format
idct_image = np.uint8(idct_image)

# Calculate PSNR between original and IDCT images
psnr = cv2.PSNR(gray_image, idct_image)

# Display the original and IDCT images along with the PSNR value
plt.figure(figsize=(10, 6))

plt.subplot(1, 3, 1)
plt.imshow(gray_image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(idct_image, cmap='gray')
plt.title('IDCT Image')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.text(0.5, 0.5, 'PSNR: {:.2f} dB'.format(psnr), ha='center', va='center', fontsize=12)
plt.axis('off')

plt.tight_layout()
plt.show()
