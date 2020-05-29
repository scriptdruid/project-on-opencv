import cv2

# import numpy as np

# matrix filled with zeros # black

img = np.zeros((512, 512))
print(img.shape)  # (512, 512) , there is no 3rd dimension

# to add dim for colors we add channels
img = np.zeros(
    (512, 512, 3), np.uint8
)  # unsigned int gives 0 -255 , 0 being black , 255 being white
print(img.shape)  # (512, 512) , there is no 3rd dimension

# to add actual colors

img = np.zeros((512, 512, 3), np.uint8)
img[:] = 255, 0, 0  # blue color to color the whole matrix
print(img.shape)


# to draw line
cv2.line(img, (0, 0), (300, 300), (0, 255, 255), 3)

# or to draw a diagonal till the end
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 255), 3)

# rectangle
# img, starting coord, ending coord, color, thickness
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 2)

# to fill the area
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), cv2.FILLED)

# circle
# img, center, radius, color, thickness
cv2.circle(img, (450, 50), 30, (0, 255, 0), cv2.FILLED)

# text on images
# img, text, origin, font , scale, color , thickness
cv2.putText(img, "HELLO WORLD", (200, 100), cv2.FONT_ITALIC, 1, (0, 0, 255), 3)

cv2.imshow("Black Image", img)
cv2.waitKey(5000)
