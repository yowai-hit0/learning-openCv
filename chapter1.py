import cv2
import numpy as np

img = cv2.imread('resources/luffr.jpg')
kernel = np.ones((5,5),np.uint8)
imageGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imageBlur = cv2.GaussianBlur(img,(7,7),0)
imgcanny = cv2.Canny(img,100,100)
imageDialation = cv2.dilate(imgcanny,kernel,iterations=1)
imageErrored  = cv2.erode(imageDialation,kernel,iterations=1)

# cv2.imshow('grey_image',imageGray)
cv2.imshow('blured image',imageBlur)
cv2.imshow('canny imgae',imgcanny)
cv2.imshow('dilation image',imageDialation)
cv2.imshow('errosion',imageErrored)
cv2.imshow('image gray' , imageGray)
cv2.waitKey(0)