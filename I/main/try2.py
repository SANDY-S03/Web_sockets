import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img = Image.open("ippr_assignment_1a_img1.jpg")
M = np.asarray(img)

plt.figure(figsize=(12, 12))
resized_image = img.resize((512, 512))

img = (resized_image)

plt.subplot(2, 2, 1)
plt.imshow(img)
plt.title("ippr_assignment_1a_img1.")
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(M[:, :, 0], cmap='Reds', vmin=0, vmax=255)
plt.title("Red Channel")
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(M[:, :, 1], cmap='Greens', vmin=0, vmax=255)
plt.title("Green Channel") 
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(M[:, :, 2], cmap='Blues', vmin=0, vmax=255)
plt.title("Blue Channel")
plt.axis('off')

plt.show()
