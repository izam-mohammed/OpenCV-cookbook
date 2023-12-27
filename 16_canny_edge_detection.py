import cv2
import matplotlib.pyplot as plt


def canny_edge_detection(path: str) -> None:
    """Detect the canny edges in the image

    Args:
        path: path to the image

    Returns:
        None
    """
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    # Apply Canny edge detection
    edges = cv2.Canny(image, 50, 150)

    # Display the results
    plt.figure(figsize=(10, 6))

    plt.subplot(1, 2, 1), plt.imshow(image, cmap="gray"), plt.title("Original Image")
    plt.subplot(1, 2, 2), plt.imshow(edges, cmap="gray"), plt.title("Canny Edges")

    plt.tight_layout()
    plt.show()
