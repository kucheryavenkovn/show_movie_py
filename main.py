import numpy as np
import cv2
import os

cap = cv2.VideoCapture('video.mp4')
cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

clicked = False
def onMouse(event, x, y, flags, param):
    global clicked
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True

cv2.setMouseCallback('window', onMouse)
success, frame = cap.read()

while (cv2.waitKey(1) == -1 and not clicked):
    if frame is not None:
        cv2.imshow('window', frame)
    else:
        cap = cv2.VideoCapture('video.mp4')
    success, frame = cap.read()

cap.release()
cv2.destroyAllWindows()