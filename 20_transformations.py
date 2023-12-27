import cv2
import numpy as np

img = cv2.imread("data/cat.jpg")
cv2.imshow("original image", img)

# transalate
def transalate(img, x, y):
    transmat = np.float32([[1, 0, x], [0,10,y]])
    dimention = img.shape[1], img.shape[0]
    return cv2.warpAffine(img, transmat, dimention)
# -x  --> left
# -y --> up
# x  --> right
# y  --> down
transalated = transalate(img, 1, 1)
cv2.imshow("transalated image", transalated)


# Rotate
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)  # take the center
    
    rotMat = cv2.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv2.warpAffine(img, rotMat, dimensions)
rotated = rotate(img, 90)
cv2.imshow("rotated", rotated)


# Flip an image
vertical_flip = cv2.flip(img, 0)
cv2.imshow("flipped vertically", vertical_flip)

horizontal_flip = cv2.flip(img,1)
cv2.imshow("flipped horizontally", horizontal_flip)




cv2.waitKey(0)