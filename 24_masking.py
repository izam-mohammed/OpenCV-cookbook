import cv2
import numpy as np

img = cv2.imread("data/nature.jpg")
cv2.imshow("original image", img)

blank = np.zeros(img.shape[:2], dtype="uint8")
cv2.imshow("blank image", blank)

mask = cv2.circle(blank.copy(), (img.shape[1] // 2, img.shape[0] // 2), 100, 255, -1)
cv2.imshow("mask image", mask)

masked_img = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("masked image", masked_img)

cv2.waitKey(0)
