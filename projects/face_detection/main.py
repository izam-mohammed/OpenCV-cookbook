import cv2


def detect_faces_webcam():
    """A function for detect face from the webcam footage

    Args:
        None

    Returns:
        None
    """

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades
        + "haarcascade_frontalface_default.xml"  # Load the pre-trained face detection classifier
    )

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            gray, scaleFactor=1.3, minNeighbors=5
        )  # Detect faces in the frame

        for x, y, w, h in faces:
            cv2.rectangle(
                frame, (x, y), (x + w, y + h), (0, 255, 0), 2
            )  # Draw rectangles around the detected faces

        cv2.imshow("Webcam - Detected Faces", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    detect_faces_webcam()
