import numpy as np
import cv2
from pathlib import Path
from logger import logger


def draw_rectangle(
    img: np.ndarray, start_point: tuple, end_point: tuple, color: tuple, thickness: int
) -> np.ndarray:
    """Draw a rectangle in the given image

    args:
        img: numpy representation of image
        start_point: starting point of rectangle
        end_point: ending point of rectangle
        color: RGB colors as a tuple eg:- (23,54,23)
        thickness: the thickness of the rectangle


    return:
        np.ndarray: numpy representation of new array
    """
    image = cv2.rectangle(img, start_point, end_point, color, thickness)
    logger.info(f"drawing a rectangle in the the image of color {color}")
    return image


def draw_line(
    img: np.ndarray, start_point: tuple, end_point: tuple, color: tuple, thickness: int
) -> np.ndarray:
    """Draw a line in the given image

    args:
        img: numpy representation of image
        start_point: starting point of line
        end_point: ending point of line
        color: RGB colors as a tuple eg:- (23,54,23)
        thickness: the thickness of the rectangle


    return:
        np.ndarray: numpy representation of new array
    """
    image = cv2.line(img, start_point, end_point, color, thickness)
    logger.info(f"drawing a line in the the image of color {color}")
    return image


def draw_circle(
    img: np.ndarray, center_cordinates: tuple, radius: int, color: tuple, thickness: int
) -> np.ndarray:
    """Draw a circle in the given image

    args:
        img: numpy representation of image
        center_cordinates: center coordinates of the circle
        radius: radius of the circle
        color: RGB colors as a tuple eg:- (23,54,23)
        thickness: the thickness of the rectangle

    return:
        np.ndarray: numpy representation of new array
    """
    image = cv2.circle(img, center_cordinates, radius, color, thickness)
    logger.info(f"drawing a circle of radius {radius} in the image")
    return image


if __name__ == "__main__":
    img = cv2.imread("/home/izam/coding/opencv/data/cat.jpg")
    img_rectangle = draw_rectangle(img, (5, 5), (220, 220), (255, 0, 0), 2)
    img_line = draw_line(img, (5, 5), (220, 220), (0, 255, 0), 2)
    img_circle = draw_circle(img, (100, 100), 100, (0, 0, 255), 2)
    cv2.imshow("cat", img_rectangle)
    cv2.waitKey(0)
