import cv2
import numpy as np
kernel = np.ones((5,5),np.uint8)
img = cv2.imread("repository/demo.jpg")
img = cv2.resize(img,(400,600))
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(img,100,100)
cv2.imshow("Image",img)
cv2.imshow("Blurred Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.waitKey(0)
