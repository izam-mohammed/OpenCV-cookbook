import cv2
import numpy as np

img = cv2.imread("data/girl.jpg")
cv2.imshow("original image", img)

hor = np.hstack((img, img))
cv2.imshow("hstacked image", hor)

ver = np.vstack((img, img))
cv2.imshow("vstacked image", ver)

cv2.waitKey(0)