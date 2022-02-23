import cv2 as cv
import numpy as np


def demo(x):
    pass

img = np.zeros((300,512,3),np.uint8)
cv.namedWindow("image")
cv.createTrackbar("Red","image",0,255,demo)
cv.createTrackbar("Green","image",0,255,demo)
cv.createTrackbar("Blue","image",0,255,demo)

switch = "0:OFF\n1:ON"
cv.createTrackbar(switch,"image",0,1,demo)

while(1):
    cv.imshow('image',img)
    r = cv.getTrackbarPos("Red","image")
    g = cv.getTrackbarPos("Green","image")
    b = cv.getTrackbarPos("Blue","image")
    s = cv.getTrackbarPos(switch,"image")
    k = cv.waitKey(1) & 0xFF
    if k==27:
        break;
    if s == 0:
        img[:]=0
    else:
        img[:] =[b,g,r]



