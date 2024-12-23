import cv2
import numpy as np
width,height = 300,350
img = cv2.imread('resources/theshoe.png')
pts1=np.float32([[140,70],[140,143],[292,18],[292,143]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow('original',img)
cv2.imshow('warped',imOutput)

cv2.waitKey(0)