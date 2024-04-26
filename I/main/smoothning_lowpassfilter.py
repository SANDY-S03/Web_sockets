import cv2

# Load the RGB noisy image
image_path = 'white_noise.png'  # Update with the actual path to your noisy image
noisy_image = cv2.imread(image_path)

if noisy_image is None:
    print("Error: Image could not be loaded. Please check the file path.")
    exit()

# Apply Gaussian blur to smoothen the image
smooth_image = cv2.GaussianBlur(noisy_image, (5, 5), 0)  # Adjust kernel size as needed

# Display the smooth image
cv2.imshow('Smooth Image', smooth_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
