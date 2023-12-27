import numpy as np
import cv2 as cv

# events
# cv2.EVENT_MOUSEMOVE: This event is triggered when the mouse pointer is moved over the window.
# cv2.EVENT_LBUTTONDOWN: Triggered when the left mouse button is pressed.
# cv2.EVENT_LBUTTONUP: Triggered when the left mouse button is released.
# cv2.EVENT_RBUTTONDOWN: Triggered when the right mouse button is pressed.
# cv2.EVENT_RBUTTONUP: Triggered when the right mouse button is released.
# cv2.EVENT_MBUTTONDOWN: Triggered when the middle mouse button is pressed.
# cv2.EVENT_MBUTTONUP: Triggered when the middle mouse button is released.
# cv2.EVENT_LBUTTONDBLCLK: Triggered when the left mouse button is double-clicked.
# cv2.EVENT_RBUTTONDBLCLK: Triggered when the right mouse button is double-clicked.
# cv2.EVENT_MBUTTONDBLCLK: Triggered when the middle mouse button is double-clicked.
# cv2.EVENT_MOUSEWHEEL: Triggered when the mouse wheel is scrolled.


def mouse_even_circle(image_path: str, action: int = cv.EVENT_LBUTTONDBLCLK) -> None:
    """Draw a circle in the given image in the given action

    Args:
        image_path: The path to the image
        action: mouse action triggered

    Returns:
        None
    """

    def drawfunction(event, x, y, flags, param):
        if event == action:
            cv.circle(img, (x, y), 20, (255, 255, 255), -1)

    img = cv.imread(image_path)
    cv.namedWindow("image")
    cv.setMouseCallback("image", drawfunction)
    while 1:
        cv.imshow("image", img)
        key = cv.waitKey(1)
        if key == 27:
            break

    cv.destroyAllWindows()


if __name__ == "__main__":
    mouse_even_circle("data/cat.jpg")
