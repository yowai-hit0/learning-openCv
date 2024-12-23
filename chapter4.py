import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
# print(img)
# img[200:300,100:500] = 55,0,0
#     height,width = value

# img[:] = 55,0,0
# for coloring the whole image

# cv2.line(img,(0,0),(300,300),(26,236,20),1)
#        img,stpnt,endpnt,color,thickness

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(26,236,20),1)
cv2.rectangle(img,(100,150),(200,250),(50,50,50),cv2.FILLED)
cv2.circle(img,(400,50),30,(78,78,26),3)
cv2.putText(img," OPEN CV ",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(89,129,123),4)
cv2.imshow('img',img)
cv2.waitKey(0)