import cv2
from matplotlib import pyplot as plt

# Load the image
image_path = '24bit_rgb.jpeg'  # Update with the actual path to your image
image = cv2.imread(image_path)

if image is None:
    print("Error: Image could not be loaded. Please check the file path.")
    exit()

# Split the image into its respective channels
channels = cv2.split(image)

# Set the colors for the histogram
colors = ('b', 'g', 'r')
labels = ['Blue Channel', 'Green Channel', 'Red Channel']

# Create a figure with 3 subplots
plt.figure(figsize=(15, 5))

# Loop through the color channels
for i, (channel, color, label) in enumerate(zip(channels, colors, labels)):
    plt.subplot(1, 3, i + 1)  # Positions: 1st, 2nd, 3rd in a 1 row by 3 columns grid
    histogram = cv2.calcHist([channel], [0], None, [256], [0, 256])
    plt.plot(histogram, color=color)
    plt.title(label)
    plt.xlim([0, 256])
    plt.ylim([0, max(histogram)*1.1])  # Optional: Adjust the y-axis to better fit the plot
    plt.xlabel('Pixel Intensity')
    if i == 0:
        plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
