import cv2

# Reading and displaying an image
img = cv2.imread("repository/demo.jpg")
img = cv2.resize(img,(400,600))
cv2.imshow("Output",img)
cv2.waitKey(0)

# Reading our webcam

cap = cv2.VideoCapture(0)
cap.set(3,480)
cap.set(4,640)
while True:
    success,img = cap.read()
    cv2.imshow("WEBCAM",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
