import cv2
import matplotlib.pyplot as plt

# Read the image in grayscale
image = cv2.imread('data/cat.jpg', cv2.IMREAD_GRAYSCALE)

# Apply Canny edge detection
edges = cv2.Canny(image, 50, 150)

# Display the results
plt.figure(figsize=(10, 6))

plt.subplot(1, 2, 1), plt.imshow(image, cmap='gray'), plt.title('Original Image')
plt.subplot(1, 2, 2), plt.imshow(edges, cmap='gray'), plt.title('Canny Edges')

plt.tight_layout()
plt.show()
