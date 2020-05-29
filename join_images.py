import cv2
import numpy as np

img = cv2.imread("data/family-1016311_640.jpg")

imgHor = np.hstack((img, img))  # these are numpy functions not opencv
imgVert = np.vstack((img, img))

# this will not work if both the images do not have same channel etc

cv2.imshow("horizontal", imgHor)
cv2.imshow("vertical", imgVert)


cv2.waitKey(10000)

# need to add custom function for multiple stacking
