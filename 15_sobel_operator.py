import cv2
import numpy as np
import matplotlib.pyplot as plt


def sobel(path: str) -> None:
    """Applying the sobel transformation to the images

    Args:
        path: The path to the image

    Returns:
        None
    """
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    # Calculate Sobel gradients
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

    # Compute the magnitude of the gradient
    gradient_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)

    # Display the results
    plt.figure(figsize=(10, 6))

    plt.subplot(2, 2, 1), plt.imshow(image, cmap="gray"), plt.title("Original Image")
    plt.subplot(2, 2, 2), plt.imshow(sobel_x, cmap="gray"), plt.title("Sobel X")
    plt.subplot(2, 2, 3), plt.imshow(sobel_y, cmap="gray"), plt.title("Sobel Y")
    plt.subplot(2, 2, 4), plt.imshow(gradient_magnitude, cmap="gray"), plt.title(
        "Gradient Magnitude"
    )

    plt.tight_layout()
    plt.show()

sobel("data/girl.jpg")
