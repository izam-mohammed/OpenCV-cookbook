import cv2
import matplotlib.pyplot as plt

img = cv2.imread("data/nature.jpg")
cv2.imshow("original image", img)

# BGR to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray scale image", gray)

# BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("hsv image", hsv)

# BGR to LAB
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow("LAB image", lab)

# BGR to RGB
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(rgb)
# plt.show()


# HSV to BGR
hsv_bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
cv2.imshow("HSV ---> BGR image", hsv_bgr)


# LAB to BGR
lab_bgr = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
cv2.imshow("LAB --> BGR image", lab_bgr)

cv2.waitKey(0)
