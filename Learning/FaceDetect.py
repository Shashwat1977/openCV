import cv2 as cv

img = cv.imread("repository/lena.png")
imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

faceCascade = cv.CascadeClassifier("repository/haarcascade_frontalface_default.xml")

faces = faceCascade.detectMultiScale(imgGray,1.1,4)
for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv.imshow("Face Detection",img)
cv.waitKey(0)