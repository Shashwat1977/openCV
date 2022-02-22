import cv2
import numpy as np

img = np.zeros((604,604,3),np.uint8)
# cv2.imshow("Blank Image",img)

# Adding colour to the image
img[:] = 255,0,0
# cv2.imshow("Coloured image",img)
cv2.line(img,(0,0),(300,300),(0,0,255),3)
cv2.circle(img,(300,300),60,(234,255,176),5)
cv2.putText(img,"OPENCV",(300,300),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,2,(255,255,255),6)
cv2.imshow("Image With Shapes",img)
cv2.waitKey(0)
