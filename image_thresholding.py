import cv2
import numpy as np


def thresholding_img(
    path: str,
    value: int,
) -> None:
    """A fuction for thresholding the image with given value

    Args:
        path: The path to the image
        value: value of the thresholding

    Returns:
        None
    """
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    # Set a threshold value (adjust as needed)
    threshold_value = 127

    # Apply binary thresholding
    _, binary_image = cv2.threshold(image, value, 255, cv2.THRESH_BINARY)

    # Display the original and thresholded images
    cv2.imshow("Original Image", image)
    cv2.imshow("Binary Thresholded Image", binary_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
