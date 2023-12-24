import cv2

# Read the image in grayscale
image = cv2.imread('data/cat.jpg', cv2.IMREAD_GRAYSCALE)

# Apply adaptive thresholding
adaptive_threshold = cv2.adaptiveThreshold(
    image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
)

# Display the original and adaptive thresholded images
cv2.imshow('Original Image', image)
cv2.imshow('Adaptive Thresholded Image', adaptive_threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
