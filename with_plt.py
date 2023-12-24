import cv2
import matplotlib.pyplot as plt

# Read the image using OpenCV
image = cv2.imread('data/cat.jpg')

# Convert BGR to RGB (Matplotlib uses RGB)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display the image using Matplotlib
plt.imshow(image_rgb)
plt.title('Image using Matplotlib')
plt.axis('on')  # Turn off axis labels
plt.show()