import cv2

# Load the Haar Cascade Classifier for face detection
face_cascade = cv2.CascadeClassifier('/assets/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)  # 0 for default camera (you can change it if you have multiple cameras)
while True:
    ret, frame = cap.read()  # Read a frame from the camera

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frameq
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('Face Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()