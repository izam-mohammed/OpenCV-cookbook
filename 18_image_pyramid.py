import cv2
import matplotlib.pyplot as plt


def image_pyramid(path: str) -> None:
    """Showing the image pyramid of images in different scales

    Args:
        The path to the image

    Returns:
        None
    """
    image = cv2.imread(path)

    # Convert BGR to RGB (Matplotlib uses RGB)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Display the original image
    plt.figure(figsize=(8, 8))
    plt.subplot(3, 3, 1), plt.imshow(image_rgb), plt.title("Original Image")

    # Build the image pyramid and display the scaled images
    for i in range(2, 10):
        # Resize the image to a fraction of the original size
        resized_image = cv2.resize(image, (image.shape[1] // i, image.shape[0] // i))

        # Convert BGR to RGB for display
        resized_image_rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)

        # Display the resized image
        plt.subplot(3, 3, i), plt.imshow(resized_image_rgb), plt.title(f"Scale {1/i}")

    plt.tight_layout()
    plt.show()


image_pyramid("data/girl.jpg")
