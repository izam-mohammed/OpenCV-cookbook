import cv2
from pathlib import Path
import numpy as np
from logger import logger


def read_image(path: Path, flag: int = 1) -> np.ndarray:
    """Reads a image

    Args:
        path: the path to the image file
        flag: the flag of the image

    return:
        pass
    """
    image = cv2.imread(str(path), flag)
    logger.info(f"loaded the image {str(path)}")

    return image


def show_image(name: str, image: np.ndarray) -> None:
    """show the cv2 image

    Args:
        name: name of the image
        image: numpy array representation of the image

    return:
        None
    """
    cv2.imshow(name + " (press any key to close)", image)
    logger.info(f"showing the image {name}")

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def save_image(path: Path, image: np.ndarray) -> bool:
    """Save the cv2 image

    args:
        path: path to the image file
        image: the numpy representation of the image
    return:
        None
    """

    saved = cv2.imwrite(str(path), image)
    logger.info(f"save file {path} status : {saved}")
    return saved


if __name__ == "__main__":
    path = Path("/home/izam/coding/opencv/data/cat.jpg")
    image = read_image(path, flag=128)
    show_image(name="cat", image=image)
    save_image(Path("artifacts/new.jpg"), image)
