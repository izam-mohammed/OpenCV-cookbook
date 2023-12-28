import cv2
import numpy as np

img = cv2.imread("data/nature.jpg")
cv2.imshow("original image", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray image", gray)

# Laplacian
lap = cv2.Laplacian(gray, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow("Laplacian image", lap)


# sobel
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1)
combined_sobel = cv2.bitwise_or(sobelx, sobely)
cv2.imshow("sobel combined image", combined_sobel)

# canny
canny = cv2.Canny(gray, 125, 175)
cv2.imshow("Canny image",canny)


cv2.waitKey(0)