import cv2
import numpy as np

# matrix filled with zeros # black

img = np.zeros((512, 512))
cv2.imshow("Black Image", img)
cv2.waitKey(5000)
