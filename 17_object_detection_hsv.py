import cv2
import numpy as np
from typing import Union, Annotated


def object_detection_hsv(
    video_source: Union[
        Annotated[int, "streaming"],
        Annotated[str, "path to image"],
    ] = 0
) -> None:
    """Perform an object detection using hsv

    args:
        video_source: the source video path or 0 if using the webcam

    Returns:
        None
    """
    cap = cv2.VideoCapture(video_source)

    while True:
        ret, frame = cap.read()

        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_color = np.array([85, 60, 60])  # Lower HSV values for the color
        upper_color = np.array([100, 100, 100])  # Upper HSV values for the color

        mask = cv2.inRange(hsv_frame, lower_color, upper_color)

        result_frame = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow("Original Frame", frame)
        cv2.imshow("Detected Object", result_frame)

        # Press 'q' to exit the loop
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    object_detection_hsv()
