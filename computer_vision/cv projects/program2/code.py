import cv2 
import random 
'''
import cv2 

img=cv2.imread('cv projects/program1/images/Elon Musk.jpg',-1)

print(img)
print(img.shape)
print(type(img))
print(img[0])
print(img[457][47:350])
print(img[457][350])











(rows, columns, channels)






'''
img=cv2.imread('cv projects/program1/images/Elon Musk.jpg',-1)

'''
for i in range(100):
    for j in range (img.shape[1]):
       img[i][j] = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]

'''

tag =  img[500:700, 600:900]

img[100:300, 650:950] = tag 
cv2.imshow('IMAGE',img)
cv2.waitKey(0)
cv2.destroyAllWindows()