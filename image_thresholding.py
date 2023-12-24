import cv2
import numpy as np

# Read the image in grayscale
image = cv2.imread('data/cat.jpg', cv2.IMREAD_GRAYSCALE)

# Set a threshold value (adjust as needed)
threshold_value = 127

# Apply binary thresholding
_, binary_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)

# Display the original and thresholded images
cv2.imshow('Original Image', image)
cv2.imshow('Binary Thresholded Image', binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
