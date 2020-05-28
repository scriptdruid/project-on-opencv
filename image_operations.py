import cv2
import numpy as np

img = cv2.imread("data/family-1016311_640.jpg")

# convert the image in greyscale

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# convert the image to blur

imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)  # odd numbers

# to find edges in images

imgCanny = cv2.Canny(
    img, 150, 200
)  # change this param to decide how evident the edges should be

# increasing the thickness of the edges - dilation
imgDilation = cv2.dilate(imgCanny, kernel=np.ones((5, 5), np.uint8), iterations=5)


# decreasing the thickness - erosion - opposite of dilation

imgErosion = cv2.erode(imgDilation, kernel=np.ones((5, 5), np.uint8), iterations=3)

# cv2.imshow("Gray Image", imgGray)
# cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dilation Image", imgDilation)
cv2.imshow("Erosion Image", imgErosion)

cv2.waitKey(10000)
