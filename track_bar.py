import cv2
import numpy as np


def update_value(value):
    # Callback function to update the image based on the trackbar value
    global img, window_name
    # Do some processing based on the trackbar value
    processed_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, processed_img = cv2.threshold(processed_img, value, 255, cv2.THRESH_BINARY)

    # Display the processed image
    cv2.imshow(window_name, processed_img)


if __name__ == "__main__":
    # Read an example image
    img = cv2.imread("data/cat.jpg")

    # Create a window and display the original image
    window_name = "Image with Trackbar"
    cv2.namedWindow(window_name)
    cv2.imshow(window_name, img)

    # Create a trackbar
    trackbar_name = "Threshold Value"
    initial_value = 128
    max_value = 255
    cv2.createTrackbar(
        trackbar_name, window_name, initial_value, max_value, update_value
    )

    # Call the update_value function once to apply the initial processing
    # update_value(initial_value)

    # Wait for the user to press a key
    cv2.waitKey(0)
    cv2.destroyAllWindows()
