import cv2


def adaptive_thresh(path: str) -> None:
    """Take the image and apply the adaptive threshold

    Arguments:
        path: path to the image

    Returns:
        None
    """
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    # Apply adaptive thresholding
    adaptive_threshold = cv2.adaptiveThreshold(
        image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
    )

    # Display the original and adaptive thresholded images
    cv2.imshow("Original Image", image)
    cv2.imshow("Adaptive Thresholded Image", adaptive_threshold)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
