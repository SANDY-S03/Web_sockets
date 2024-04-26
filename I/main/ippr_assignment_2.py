
from PIL import Image
import matplotlib.pyplot as plt

def neg_trans(img):
    width, height = img.size

    for x in range(width):
        for y in range(height):
            pixel_color = img.getpixel((x, y))

            if type(pixel_color) == tuple: 
                
                red_pixel = 256 - 1 - pixel_color[0]
                green_pixel = 256 - 1 - pixel_color[1]
                blue_pixel = 256 - 1 - pixel_color[2]

                img.putpixel((x, y), (red_pixel, green_pixel, blue_pixel))
            
            else:
                pixel_color = 256 - 1 - pixel_color 

                img.putpixel((x, y), pixel_color)
    return img

image = Image.open('ippr_assignment_1a_img1.jpg')
resized_image = image.resize((512, 512))

negative_image = neg_trans(resized_image)

plt.subplot(1, 2, 1)
plt.axis('off')
plt.imshow(image)
plt.title("ippr_assignment_1a_img1")

plt.subplot(1, 2, 2)
plt.axis('off')

plt.imshow(negative_image)
plt.title("Negative Image")

plt.show()