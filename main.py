import cv2

capture = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")

while True:
    _,frame = capture.read()

    grayScaled = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(grayScaled,1.1,6)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)

    cv2.imshow("Webcam",frame)
    if cv2.waitKey(1)==ord('e'):
        break
capture.release()
cv2.destroyAllWindows()

