import cv2 

img = cv2.imread('cv projects/program1/images/Elon Musk.jpg',-1)

print(img)
print(img.shape)
print(type(img))
print(img[0])
print(img[457][47:350])
print(img[457][350])