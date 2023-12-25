import cv2
import numpy as np
import matplotlib.pyplot as plt
from typing import Annotated


def morphological_transform(path: Annotated[str, "Binary image"]) -> None:
    """Perform morphological transformation in given image

    Args:
        path: The path to the image

    Returns:
        None
    """
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    # Create a kernel for morphological operations
    kernel = np.ones((10, 10), np.uint8)

    # Dilation: Expands white regions in the image
    dilated_image = cv2.dilate(image, kernel, iterations=1)

    # Erosion: Shrinks white regions in the image
    eroded_image = cv2.erode(image, kernel, iterations=1)

    # Opening: Erosion followed by dilation
    opening_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

    # Closing: Dilation followed by erosion
    closing_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

    # Display the images
    plt.figure(figsize=(10, 6))

    plt.subplot(2, 3, 1), plt.imshow(image, cmap="gray"), plt.title("Original Image")
    plt.subplot(2, 3, 2), plt.imshow(dilated_image, cmap="gray"), plt.title(
        "Dilated Image"
    )
    plt.subplot(2, 3, 3), plt.imshow(eroded_image, cmap="gray"), plt.title(
        "Eroded Image"
    )
    plt.subplot(2, 3, 4), plt.imshow(opening_image, cmap="gray"), plt.title(
        "Opening Image"
    )
    plt.subplot(2, 3, 5), plt.imshow(closing_image, cmap="gray"), plt.title(
        "Closing Image"
    )

    plt.tight_layout()
    plt.show()
