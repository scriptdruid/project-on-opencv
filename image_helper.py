import cv2


# How to read images, videos, camera
# Read images

img = cv2.imread("data/family-1016311_640.jpg")
cv2.imshow("output", img)
cv2.waitKey(10000)

# to read video

vid = cv2.VideoCapture("data/smelly_cat.mp4")

# Since video is sequence of images , we will use while loop to go through each image
while True:
    status, img_seq = vid.read()
    cv2.imshow("video", img_seq)
    # wait until key q is pressed on keyboard
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# using a webcam

cam = cv2.VideoCapture(0)  # uses the default webcam
cam.set(3, 640)  # width
cam.set(4, 480)  # height
cam.set(10, 100)  # brightness

# Since video is sequence of images , we will use while loop to go through each image
while True:
    status, img_seq = cam.read()
    cv2.imshow("video", img_seq)
    # wait until key q is pressed on keyboard
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
