import cv2
import numpy as np

img = cv2.imread("repository/demo.jpg")
img = cv2.resize(img,(400,600))

# Cropping an image
imgCrop = img[100:400]
cv2.imshow("Image",img)
cv2.imshow("Cropped Image",imgCrop)
cv2.waitKey(0)