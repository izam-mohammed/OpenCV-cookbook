import cv2
img = cv2.imread("data/cat.jpg")
cv2.imshow("original cat", img)

# convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.imshow("gray", gray)

# blur img
blur = cv2.GaussianBlur(img, (9,9), cv2.BORDER_DEFAULT)
cv2.imshow("blur", blur)

# edge cascade
canny = cv2.Canny(img, 125, 175)
cv2.imshow("canny", canny)

# dialiating
dialated = cv2.dilate(canny, (7, 7), iterations=3)
cv2.imshow("Dialated", dialated)

# eroding
eroded = cv2.erode(dialated, (3, 3), iterations=3)
cv2.imshow('eroded', eroded)

# resize
resized = cv2.resize(img, (200, 200), interpolation=cv2.INTER_CUBIC)
cv2.imshow("resized", resized)

# croped
croped = img[50:150, 200:350]
cv2.imshow("croped", croped)

cv2.waitKey(0)