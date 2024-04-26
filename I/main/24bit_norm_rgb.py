import cv2
import numpy as np
import ctypes

# Function to get screen dimensions
def get_screen_dimensions():
    user32 = ctypes.windll.user32
    width, height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    return width, height

# Load the RGB image
image_path = 'img2.jpg'  # Update with the actual path to your image
image = cv2.imread(image_path).astype(np.float32)

if image is None:
    print("Error: Image could not be loaded. Please check the file path.")
    exit()

# Normalize the image to the range [0, 1]
normalized_image = image / 255.0

# Ensure values are within the valid range
normalized_image = np.clip(normalized_image, 0, 1)

# Get screen dimensions
screen_width, screen_height = get_screen_dimensions()

# Resize the image to fit within the screen dimensions
scaled_image = cv2.resize(normalized_image, (screen_width - 100, screen_height - 100))

# Display the normalized image
cv2.imshow('Normalized Image', scaled_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
