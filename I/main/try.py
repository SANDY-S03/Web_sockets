import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Open the original image
img = Image.open("ippr_assignment_1a_img1.jpg")

# Invert the image by 180 degrees
inverted_img = img.rotate(180)

# Convert the inverted image to a NumPy array
M_inverted = np.asarray(inverted_img)

# Plotting
plt.figure(figsize=(12, 12))

# Original Image
plt.subplot(2, 3, 1)
plt.imshow(img)
plt.title("Original Image")
plt.axis('off')

# Inverted Image
plt.subplot(2, 3, 2)
plt.imshow(inverted_img)
plt.title("Inverted Image (180 degrees)")
plt.axis('off')

# Red Channel
plt.subplot(2, 3, 3)
plt.imshow(M_inverted[:, :, 0], cmap='Reds', vmin=0, vmax=255)
plt.title("Inverted Red Channel")
plt.axis('off')

# Green Channel
plt.subplot(2, 3, 4)
plt.imshow(M_inverted[:, :, 1], cmap='Greens', vmin=0, vmax=255)
plt.title("Inverted Green Channel")
plt.axis('off')

plt.subplot(2, 3, 5)
plt.imshow(M_inverted[:, :, 2], cmap='Blues', vmin=0, vmax=255)
plt.title("Inverted Blue Channel")
plt.axis('off')

plt.show()
