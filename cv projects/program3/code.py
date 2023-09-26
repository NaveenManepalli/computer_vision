import numpy as np
import cv2

ip_address =input("enter the ip addrress of your mobile webcam:")

port ="your_port"

url = f"http://{ip_address}:{port}/video"


cap =cv2.VideoCapture(url)

while True:
    ret, frame =cap.read()
    

    image = np.zeros(frame.shape,np.uint8)

    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()