import cv2
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('img2.jpg')

# Define the scaling factors
scale_factor_2x = 2.0
scale_factor_0_5x = 0.5

# Perform scaling
scaled_image_2x = cv2.resize(image, None, fx=scale_factor_2x, fy=scale_factor_2x, interpolation=cv2.INTER_LINEAR)
scaled_image_0_5x = cv2.resize(image, None, fx=scale_factor_0_5x, fy=scale_factor_0_5x, interpolation=cv2.INTER_LINEAR)

# Display the original and scaled images using matplotlib
plt.figure(figsize=(10, 6))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(scaled_image_2x, cv2.COLOR_BGR2RGB))
plt.title('Scaled by 2x')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(scaled_image_0_5x, cv2.COLOR_BGR2RGB))
plt.title('Scaled by 0.5x')
plt.axis('off')

plt.tight_layout()
plt.show()
