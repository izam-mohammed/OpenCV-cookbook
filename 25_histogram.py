import cv2
import matplotlib.pyplot as plt

img = cv2.imread("data/nature.jpg")
cv2.imshow("original image", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("grayscale", gray)

# graysclae histogram
gray_hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

plt.figure()
plt.title("grayscale histogram")
plt.xlabel("bins")
plt.ylabel("# of pixels")
plt.plot(gray_hist)
plt.xlim([0, 256])
# plt.show()


# color histogram

plt.figure()
plt.title("colored histogram")
plt.xlabel("bins")
plt.ylabel("# of pixels")
colors = ("b", "g", "r")
for i, col in enumerate(colors):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 255])
plt.show()


cv2.waitKey(0)