import cv2
import numpy as np

def object_detection_hsv(video_source=0):
    # Open a connection to the video source (0 represents the default camera)
    cap = cv2.VideoCapture(video_source)

    while True:
        # Read a frame from the video stream
        ret, frame = cap.read()

        # Convert the frame from BGR to HSV color space
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Define the HSV color range for the object you want to detect (adjust these values)
        lower_color = np.array([30, 50, 50])  # Lower HSV values for the color
        upper_color = np.array([60, 255, 255])  # Upper HSV values for the color

        # Create a mask to extract the object based on the color range
        mask = cv2.inRange(hsv_frame, lower_color, upper_color)

        # Bitwise-AND operation to extract the object from the original frame
        result_frame = cv2.bitwise_and(frame, frame, mask=mask)

        # Display the original frame and the result with the detected object
        cv2.imshow('Original Frame', frame)
        cv2.imshow('Detected Object', result_frame)

        # Press 'q' to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video stream and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    object_detection_hsv()