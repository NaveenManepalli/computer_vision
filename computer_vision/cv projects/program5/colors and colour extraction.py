import numpy as np
import cv2

ip_address =input("enter the ip addrress of your mobile webcam:")

port ="your_port"

url = f"http://{ip_address}:{port}/video"


cap =cv2.VideoCapture(url)

while True:
    ret, frame =cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv =cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    lower_blue =np.array([90, 50, 50])
    upper_blue =np.array([130, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame',result)

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()