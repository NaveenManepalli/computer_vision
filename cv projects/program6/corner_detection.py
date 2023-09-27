import numpy as np
import cv2

img = cv2.imread('C:/Users/Lenovo/Desktop/computer_vision/cv projects/program6/picture/chessboard.png')

img = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Use BGR2GRAY for grayscale conversion

corners = cv2.goodFeaturesToTrack(img_gray, 100, 0.01, 10)
corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x,y), 5, (255, 0, 0), -1)

cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
