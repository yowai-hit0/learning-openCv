import cv2
import numpy as np

frameWidth = 600
frameHeight = 600
cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,100)
myColors = [
    [90,98,90,122,255,255],
    [0,93,220,179,255,255]
]
myColorValue = [
    [134,4,4],[17,88,255]
]
myPoints = []
def findColor(img,myColors,myColorValue):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    count=0
    newPoints = []
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x,y = getContours(mask)
        cv2.circle(imageContour,(x,y),5,myColorValue[count],cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count+=1
    return newPoints
def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>300:
            # cv2.drawContours(imageContour, cnt, -1, (255, 0, 235), 2)
            perimeter = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*perimeter,True)
            x,y,w,h = cv2.boundingRect(approx)
    return x+w//2,y

def drawOnCanva(mypoints,myColorValue):
    for points in mypoints:
        cv2.circle(imageContour,(points[0],points[1]),15,myColorValue[points[2]],cv2.FILLED)
while True:
    success,img = cap.read()
    imageContour = img.copy()
    newPoints = findColor(img,myColors,myColorValue)
    if len(newPoints)!=0:
        for newPt in newPoints:
            myPoints.append(newPt)
    if len(myPoints)!=0:
        drawOnCanva(myPoints,myColorValue)
    cv2.imshow('vid',imageContour)
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break