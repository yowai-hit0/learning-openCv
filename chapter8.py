import cv2
import numpy as np

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area>100:
            cv2.drawContours(imageContour, cnt, -1, (255, 0, 235), 2)
            perimeter = cv2.arcLength(cnt,True)
            print(perimeter)
            approx = cv2.approxPolyDP(cnt,0.02*perimeter,True)
            print(len(approx))
            obtConers = len(approx)
            x,y,w,h = cv2.boundingRect(approx)
            if obtConers ==3:objectType = "triangle"
            elif obtConers ==4:
                aspectRation = w/float(h)
                if aspectRation >0.85 and aspectRation<1.5:objectType='square'
                else:objectType='rectangle'
            elif obtConers>4:objectType='circles'
            else:objectType= 'none'
            cv2.rectangle(imageContour,(x,y),(x+w,y+h),(0,255,30),2 )
            cv2.putText(imageContour,objectType ,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(20,20,20),1)
        # if area>500:
        #     cv2.drawContours(imageContour, cnt, -1, (255, 0, 235), 2)
#         this use for reducing the noise or small areas of contours


img = cv2.imread('resources/yas.png')
imageContour = img.copy()
imgGrey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGrey,(7,7),1)
imgCanny =cv2.Canny(imgBlur,10,10)
getContours(imgCanny)

imgBlank = np.zeros_like(img)
# cv2.imshow('image grey',imgGrey)
# cv2.imshow('imageBlur',imgBlur)
cv2.imshow('imageCAnny',imgCanny)
cv2.imshow('imageContour',imageContour)
# cv2.imshow('blank',imgBlank)
cv2.waitKey(0)

