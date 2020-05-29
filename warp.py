import cv2
import numpy as np

# to do again

img = cv2.imread("data/cards_stacked.jpg")
img = cv2.resize(img, (800, 500))
pts1 = np.float32([[562, 112], [606, 462], [395, 354], [782, 219]])

# define cornes
width, height = 250, 350

pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("cards stacked", img)
cv2.imshow("warped image", imgOutput)
cv2.waitKey(10000)
