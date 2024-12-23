import cv2
import numpy as np

img=cv2.imread('resources/luffr.jpg')
print(img.shape)

imgResize = cv2.resize(img,(400,500))

imgCrop = img[0:200,0:300]
cv2.imshow('col',img)
# cv2.imshow('resized',imgResize)
cv2.imshow('croped',imgCrop)
cv2.waitKey(0)