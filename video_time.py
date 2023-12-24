import cv2
from datetime import datetime as dt
from typing_extensions import Union
from logger import logger

def show_webcam(
        show_date: bool=True,
        video_path: Union[int, str] = 0,) -> None:

    """Get the webcam footage and show
    
    args:
        show_date: set True if you want to show the time in the video
    returns:
        None
    """
    cap = cv2.VideoCapture(video_path)

    if video_path and not cap.isOpened():
        logger.error("Error: Could not open video file.")
        return

    while True:
        ret, frame = cap.read()

        # Add the current time to the frame
        if show_date:
            current_time = dt.now().strftime("%Y-%m-%d %H:%M:%S")
            org = (10, 30)
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 0.7
            color = (0, 0, 0)
            thickness = 1
            frame = cv2.putText(img=frame,
                                text=f'Time: {current_time}', 
                                org=org, 
                                fontFace=font, 
                                fontScale=font_scale, 
                                color=color, 
                                thickness=thickness)

        cv2.imshow('Webcam with Time', frame)

        # break if q is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    
    logger.info("closed the screen")
    
    # release the webcam and close the screen
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    show_webcam(show_date=True)