import cv2
from logger import logger

img = cv2.imread("data/group.jpg")
cv2.imshow("original image", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray image", gray)

haar_casecade = cv2.CascadeClassifier("xml_files/haar_face.xml")
faces_rect = haar_casecade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)
logger.info(f"Number of faces found - {len(faces_rect)}")

# drawing rectangle on faces
for (x, y, w, h) in faces_rect:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("with faces", img)

cv2.waitKey(0)