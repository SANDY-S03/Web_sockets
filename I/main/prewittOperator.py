import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('img2.jpg')

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Prewitt operator
kernel_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=np.float32)
kernel_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]], dtype=np.float32)

prewittx = cv2.filter2D(gray, -1, kernel_x)
prewitty = cv2.filter2D(gray, -1, kernel_y)

# Combine the x and y gradients
prewitt_combined = np.sqrt(np.square(prewittx) + np.square(prewitty))

# Normalize the combined gradients
prewitt_normalized = (prewitt_combined / np.max(prewitt_combined) * 255).astype(np.uint8)

# Plot the result using matplotlib
plt.imshow(prewitt_normalized, cmap='gray')
plt.title('Prewitt Edges')
plt.axis('off')
plt.show()
