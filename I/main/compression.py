import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load the image
image = cv2.imread('img2.jpg')

# Convert the image to RGB (OpenCV uses BGR by default)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Define the JPEG compression quality factor (0-100, higher is better quality)
quality_factor = 50  # Adjust this value as needed

# Encode the image with JPEG compression
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality_factor]
_, compressed_image = cv2.imencode('.jpg', image_rgb, encode_param)

# Decode the compressed image
decompressed_image = cv2.imdecode(compressed_image, cv2.IMREAD_COLOR)

# Calculate PSNR between original and decompressed images
psnr = cv2.PSNR(image_rgb, decompressed_image)

# Display the original and decompressed images along with the PSNR value
plt.figure(figsize=(10, 6))

plt.subplot(1, 3, 1)
plt.imshow(image_rgb)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(decompressed_image)
plt.title('Decompressed Image (Quality Factor: {})'.format(quality_factor))
plt.axis('off')

plt.subplot(1, 3, 3)
plt.text(0.5, 0.5, 'PSNR: {:.2f} dB'.format(psnr), ha='center', va='center', fontsize=12)
plt.axis('off')

plt.tight_layout()
plt.show()
