import cv2
import numpy as np
import matplotlib.pyplot as plt

def normalize_image(image):
   
    img_normalized = cv2.normalize(image, None, 0, 1.0,
    cv2.NORM_MINMAX, dtype=cv2.CV_32F)
   
  
    return img_normalized

def rgb_to_cmy(rgb_image):

    normalized_rgb = normalize_image(rgb_image)

    c = 1.0 - normalized_rgb[:, :, 0]  # Cyan
    m = 1.0 - normalized_rgb[:, :, 1]  # Magenta
    y = 1.0 - normalized_rgb[:, :, 2]  # Yellow

   
    cmy_image = np.stack((c, m, y), axis=-1)

    return cmy_image

rgb_image = cv2.imread('ippr_assignment_1a_img1.jpg')


normalized_image = normalize_image(rgb_image)

cmy_image = rgb_to_cmy(rgb_image)


plt.figure(figsize=(12, 4))


plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(rgb_image, cv2.COLOR_BGR2RGB))
plt.title('Original RGB Image')
plt.axis('on')


plt.subplot(1, 3, 2)
plt.imshow(normalized_image)
plt.title('Normalized Image')
plt.axis('on')


plt.subplot(1, 3, 3)
plt.imshow(cmy_image)
plt.title('CMY Image')
plt.axis('on')

plt.show()