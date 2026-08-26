import cv2  
import serial

ser = serial.Serial('COM3', 9600)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
# kamera acma


while True:
    ret, frame = cap.read()
    # Kameradan bir kare alip "frame" degiskenine kaydediyoruz

    faces = face_cascade.detectMultiScale(frame, 1.1, 4)
    # Bu karede yuz var mi

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # Kutu cizme 
        center_x = x + w // 2
        center_y = y + h // 2
        angle_x = int((center_x / 640) * 180)
        angle_y = int((center_y / 480) * 180)
        print(angle_x, angle_y)
        ser.write(f"{angle_x},{angle_y}\n".encode())
    cv2.imshow('Kamera', frame)

    # Sonucu ekranda goster

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #   q  tusuna basilirsa cik

cap.release()
cv2.destroyAllWindows()
# kamerayi birak ve pencereleri kapat