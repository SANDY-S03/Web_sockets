import cv2
import numpy as np
import matplotlib.pyplot as plt
import pywt

# Load the image
image = cv2.imread('img2.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply DWT (Discrete Wavelet Transform)
coeffs = pywt.dwt2(gray_image, 'haar')
cA, (cH, cV, cD) = coeffs

# Apply inverse DWT (IDWT) to retrieve the image
idwt_image = pywt.idwt2((cA, (cH, cV, cD)), 'haar')

# Convert back to uint8 format
idwt_image = np.uint8(idwt_image)

# Calculate PSNR between original and IDWT images
psnr = cv2.PSNR(gray_image, idwt_image)

# Display the original and IDWT images along with the PSNR value
plt.figure(figsize=(10, 6))

plt.subplot(1, 3, 1)
plt.imshow(gray_image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(idwt_image, cmap='gray')
plt.title('IDWT Image')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.text(0.5, 0.5, 'PSNR: {:.2f} dB'.format(psnr), ha='center', va='center', fontsize=12)
plt.axis('off')

plt.tight_layout()
plt.show()
