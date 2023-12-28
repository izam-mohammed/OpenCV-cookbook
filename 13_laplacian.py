import cv2
import numpy as np
import matplotlib.pyplot as plt


def perform_lapacian(path: str) -> None:
    """A function that perform the lapacian smoothing in image

    Args:
        path: The path to the image

    Returns:
        None
    """
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    # Apply Gaussian blur to the image
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

    # Apply Laplacian filter for edge detection
    laplacian = cv2.Laplacian(blurred_image, cv2.CV_64F)

    # Convert to uint8 for display
    laplacian = np.uint8(np.absolute(laplacian))

    # Display the results
    plt.figure(figsize=(10, 6))

    plt.subplot(1, 3, 1), plt.imshow(image, cmap="gray"), plt.title("Original Image")
    plt.subplot(1, 3, 2), plt.imshow(blurred_image, cmap="gray"), plt.title(
        "Gaussian Blur"
    )
    plt.subplot(1, 3, 3), plt.imshow(laplacian, cmap="gray"), plt.title(
        "Laplacian Edge Detection"
    )

    plt.tight_layout()
    plt.show()

perform_lapacian("data/girl.jpg")
