import cv2
import matplotlib.pyplot as plt


def with_plt(path: str) -> None:
    """show the image using matplotlib

    Args:
        path: The path to the image

    Returns:
        None
    """
    image = cv2.imread(path)

    # Convert BGR to RGB (Matplotlib uses RGB)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Display the image using Matplotlib
    plt.imshow(image_rgb)
    plt.title("Image using Matplotlib")
    plt.axis("on")  # Turn off axis labels
    plt.show()
