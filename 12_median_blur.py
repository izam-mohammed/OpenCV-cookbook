import cv2
import matplotlib.pyplot as plt


def median_blur(
    path: str,
    value: int,
) -> None:
    """A function to perform a median blur in an image

    Args:
        path: The path to the image
        value: The value of the blur parameter

    Returns:
        None
    """
    image = cv2.imread(path)

    # Convert BGR to RGB (Matplotlib uses RGB)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Apply Gaussian blur
    blurred_image = cv2.medianBlur(image_rgb, 25)

    # Display the original and blurred images
    plt.figure(figsize=(10, 6))

    plt.subplot(1, 2, 1), plt.imshow(image_rgb), plt.title("Original Image")
    plt.subplot(1, 2, 2), plt.imshow(blurred_image), plt.title("Blurred Image")

    plt.tight_layout()
    plt.show()
