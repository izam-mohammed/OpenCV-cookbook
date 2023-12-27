import cv2
import numpy as np

img = cv2.imread("data/cat.jpg")
cv2.imshow("original image", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)

canny = cv2.Canny(img, 125, 175) 
cv2.imshow("canny edges", canny)

# contours
contours, hierarchies = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
print(f"{len(contours)} contours found in the image")


blur = cv2.GaussianBlur(gray, (5, 5), cv2.BORDER_DEFAULT)
canny_blurred = cv2.Canny(blur, 125, 175)
contours, hierarchies = cv2.findContours(canny_blurred, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
print(f"{len(contours)} contours found after blurring")


# threshold
ret, thresh = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)
cv2.imshow("thresholded image", thresh)

contours, hierarchies = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
print(f"{len(contours)} contours found in the thresholded image")


blank = np.zeros(img.shape, dtype="uint8")
cv2.imshow("blank image", blank)


# drawing the contours
cv2.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv2.imshow("contours in a blank image", blank)


cv2.waitKey(0)