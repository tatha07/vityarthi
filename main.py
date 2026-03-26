import cv2
import time
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
distracted_start_time = None
DISTRACTION_THRESHOLD = 2.0  
cap = cv2.VideoCapture(0)
print("Starting Program Press 'q' to quit.")
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame. Is another app using the camera?")
        break
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    distracted = True
    status_text = "LOOKING AWAY (NO FACE)"
    color = (0, 0, 255) 
    if len(faces) > 0:
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi_gray = gray[y:y+int(h/2), x:x+w]
            roi_color = frame[y:y+int(h/2), x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=3)
            if len(eyes) >= 1:
                distracted = False
                status_text = "FOCUSED"
                color = (0, 255, 0) 
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
            else:
                status_text = "LOOKING DOWN (NO EYES)"
                color = (0, 165, 255)
    if distracted:
        if distracted_start_time is None:
            distracted_start_time = time.time()
        if (time.time() - distracted_start_time) > DISTRACTION_THRESHOLD:
            cv2.rectangle(frame, (0, 0), (frame.shape[1], frame.shape[0]), (0, 0, 255), 10)
            cv2.putText(frame, "WARNING: DISTRACTION DETECTED!", (50, 100), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
    else:
        distracted_start_time = None
        cv2.putText(frame, "FOCUS LOCKED", (50, 100), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, f"Status: {status_text}", (20, 40), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
    cv2.imshow('FocusGuard.AI', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()