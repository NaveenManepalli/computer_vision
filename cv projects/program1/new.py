import cv2
img=cv2.imread('cv projects/program1/images/Elon Musk.jpg',-1)


'''
cv2.IMREAD_COLOR  : loads a color image .any transperency of image = -1
cv2.IMREAD_GRAYSCALE : loads image is grayscale mode               = 0
cv2.IMREAD_UNCHANGED : loads image as such including alpha channel = 1

'''


img =cv2.resize(img,(0,0),fx=0.5 ,fy=0.5)

img =cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite('new_img.jpg',img)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows