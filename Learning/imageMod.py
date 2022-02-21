import cv2

img = cv2.imread("repository/demo.jpg");
img = cv2.resize(img,(400,600))
cv2.imshow("IMAGE",img)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grey Image",imgGray)

imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
cv2.imshow("Blurred Image",imgBlur)

cv2.waitKey(0)