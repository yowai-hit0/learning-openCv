import cv2
# face_cascade = cv2.CascadeClassifier('')
image = cv2.imread('resources/us.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier("C:/Users/PC/PycharmProjects/pythonProject4/venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
faces = face_cascade.detectMultiScale(gray,1.3,6)
# Draw rectangles around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (215, 2, 12),4)

# Display the output
cv2.imshow('Faces', image)
cv2.waitKey(0)
