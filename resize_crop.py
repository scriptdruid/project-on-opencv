import cv2
import numpy as np

# In mathematics the postive x axis is towards east , y towards north
# In opencv the postive x axis is towards east , same but y axis is towards south ie bottom

# Before resizing the image we need to know the current size of the image

# to know the size of the image
img = cv2.imread("data/family-1016311_640.jpg")
print(img.shape)
# (423, 640, 3) h, w, channels(bgr)

imgResize = cv2.resize(img, (300, 200))
print(imgResize.shape)
# (200, 300, 3)


# Cropping an image , using matrix  , height comes first compared to width which comes in opencv functions
imgCropped = img[0:200, 200:500]


cv2.imshow("output", img)
cv2.imshow("resized image", imgResize)
cv2.imshow("cropped image", imgCropped)
cv2.waitKey(10000)
