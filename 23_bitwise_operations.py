import cv2
import numpy as np

blank = np.zeros((400, 400), dtype="uint8")
rectangle = cv2.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv2.circle(blank.copy(), (200, 200), 200, 255, -1)
cv2.imshow("blank image", blank)
cv2.imshow("rectangle image", rectangle)
cv2.imshow("circle image", circle)

# bitwise AND  --> return the intersection
bitwise_and = cv2.bitwise_and(rectangle, circle)
cv2.imshow("bitwise_and image", bitwise_and)

# bitwise OR --> return the union
bitwise_or = cv2.bitwise_or(rectangle, circle)
cv2.imshow("bitwise_or image", bitwise_or)

# bitwise XOR  --> return the non intersection region
bitwise_xor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("bitwise xor image", bitwise_xor)

# bitwise NOT --> inverse the binary color
bitwise_not = cv2.bitwise_not(circle)
cv2.imshow("bitwise not image", bitwise_not)

cv2.waitKey(0)