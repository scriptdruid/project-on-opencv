# Using the Viola and Jones method

# Postive - Faces
# Negatives - Non Faces (Anything)
# Train the model , here we will use pretrained models

import cv2

faceCascade = cv2.CascadeClassifier(
    "data/resources/haarcascade_frontalface_default.xml"
)

img = cv2.imread("data/family-1016311_640.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

# create bounding box through all the faces we have detected
# img , starting points , corner p÷oints or diagonal , color , thickness

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# detected the face and created  a bounding box

cv2.imshow("base photo", img)

cv2.waitKey(0)
