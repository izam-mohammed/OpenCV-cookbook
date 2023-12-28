import cv2
import numpy as np


def update_hsv_trackbar(value):
    hue = cv2.getTrackbarPos("Hue", "Adjust HSV")
    saturation = cv2.getTrackbarPos("Saturation", "Adjust HSV")
    value = cv2.getTrackbarPos("Value", "Adjust HSV")

    hsv_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)
    hsv_image[:, :, 0] += hue
    hsv_image[:, :, 1] += saturation
    hsv_image[:, :, 2] += value

    updated_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

    cv2.imshow("Adjust HSV", updated_image)


original_image = cv2.imread("data/nature.jpg")
cv2.namedWindow("Adjust HSV")

cv2.createTrackbar("Hue", "Adjust HSV", 0, 360, update_hsv_trackbar)
cv2.createTrackbar("Saturation", "Adjust HSV", 0, 255, update_hsv_trackbar)
cv2.createTrackbar("Value", "Adjust HSV", 0, 255, update_hsv_trackbar)

cv2.setTrackbarPos("Hue", "Adjust HSV", 0)
cv2.setTrackbarPos("Saturation", "Adjust HSV", 0)
cv2.setTrackbarPos("Value", "Adjust HSV", 0)

cv2.imshow("Adjust HSV", original_image)

while True:
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # 27 is the ASCII code for the 'Esc' key
        break

cv2.destroyAllWindows()
