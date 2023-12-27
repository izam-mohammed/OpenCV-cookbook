import cv2
from pathlib import Path
from 01_intro import read_image, show_image
from typing import Tuple
from typing_extensions import Annotated
import numpy as np
from logger import logger


def split_image(
    path: Path,
    show: bool = False,
) -> Tuple[
    Annotated[np.ndarray, "Blue"],
    Annotated[np.ndarray, "Green"],
    Annotated[np.ndarray, "Red"],
]:
    """Split image into channels

    args:
        path: path for the image
        show: whether show all images or not

    returns:
        annotated tuple of the 3 channels in the image
    """
    img = read_image(path)
    B, G, R = cv2.split(img)
    logger.info(f"splitted the image {path} into 3 channels")

    if show:
        show_image(
            image=cv2.merge([B, np.zeros_like(G), np.zeros_like(R)]), name="Blue"
        )
        show_image(
            image=cv2.merge([np.zeros_like(B), G, np.zeros_like(R)]), name="Green"
        )
        show_image(image=cv2.merge([np.zeros_like(B), np.zeros_like(G), R]), name="Red")

    return B, G, R


def scale_image(img: np.ndarray, scale_factor: float) -> np.ndarray:
    """scale an image and return the scaled image

    Args:
        img: image that should scale
        scale_factor: The amout of resizing the image

    Returns:
        The scaled image
    """
    original_height, original_width = img.shape[:2]

    # Calculate the new dimensions based on the scale factor
    new_width = int(original_width * scale_factor)
    new_height = int(original_height * scale_factor)

    # Resize the image
    scaled_img = cv2.resize(img, (new_width, new_height))

    return scaled_img


if __name__ == "__main__":
    # split_image(path=Path("/home/izam/coding/opencv/data/cat.jpg"), show=True)
    img = read_image(path=Path("/home/izam/coding/opencv/data/cat.jpg"))
    show_image(image=img, name="original image")
    scaled_image = scale_image(img, 0.5)
    show_image(image=scaled_image, name="resized image")
