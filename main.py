import cv2
# import numpy
# import cv2
# img=cv2.imread('orig.jpg')
# cv2.imshow('output',img)
# cv2.waitKey(0)
# vid = cv2.VideoCapture('thanks.mp4')

# cap = cv2.VideoCapture('thanks.mp4')
# while True:
#     success,img = cap.read()
#     cv2.imshow('video',img)
#     if cv2.waitKey(1) & 0xFF == ord('a'):
#         break

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,600)
cap.set(10,100)
while True:
    sucess,img = cap.read()
    cv2.imshow('video',img)
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break
