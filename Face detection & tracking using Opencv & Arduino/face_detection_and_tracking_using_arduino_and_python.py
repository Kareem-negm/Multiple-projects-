"""
Face Tracking System Using Arduino - Python Code.
Close the Arduino IDE before running this code to avoid Serial conflicts.
Replace 'COM3' with the name of port where you arduino is connected.
Upload the Arduino code before executing this code.
"""
import cv2 as cv
import serial
import time

arduino = serial.Serial('COM3', 9600)
time.sleep(2)

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)
print(f"width = {cap.get(3)} , height = {cap.get(4)}")
print("Connection to arduino...")
while (cap.isOpened):
    ret, img = cap.read()

    cv.resizeWindow('face detection', 640, 480)

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1)

    font = cv.FONT_HERSHEY_SIMPLEX
    img = cv.putText(img, 'EVEREST TEAM', (265, 25), font, 0.6,
                     (255, 255, 0), 1, cv.LINE_AA, 0)

    for (x, y, w, h) in faces:
        cv.circle(img, (int(x+(w/2)), int(y+(h/2))),
                  (int((h+w)/4)), (0, 255, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        arr = {y: y+h, x: x+w}
        print(arr)

        xx = int((x+(x+h))/2)
        yy = int((y+(y+w))/2)

        center = f'({xx},{yy})'
        img = cv.putText(img, center, (280, 440), font, 0.5,
                         (220, 0, 0), 1, cv.LINE_AA, 0)

        # sending data to arduino
        data = "X{0:d}Y{1:d}Z".format(xx, yy)
        print("serial_output = '" + data + "'")
        arduino.write(data.encode('utf-8'))

    cv.imshow('face detection', img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
