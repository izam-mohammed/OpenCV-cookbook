import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('data/cat.jpg')

# Convert BGR to RGB (Matplotlib uses RGB)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Apply Gaussian blur
blurred_image = cv2.blur(image_rgb, (5,5))

# Display the original and blurred images
plt.figure(figsize=(10, 6))

plt.subplot(1, 2, 1), plt.imshow(image_rgb), plt.title('Original Image')
plt.subplot(1, 2, 2), plt.imshow(blurred_image), plt.title('Blurred Image')

plt.tight_layout()
plt.show()