import cv2 as cv

cap = cv.VideoCapture(0)
faceCascade = cv.CascadeClassifier('repository/haarcascade_frontalface_default.xml')
while True:
    res,frame = cap.read()
    frameGray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(frameGray,1.1,4)
    for (x,y,w,h) in faces:
        cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    cv.imshow("Output",frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()