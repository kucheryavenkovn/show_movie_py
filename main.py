import numpy as np
import cv2
import os
import win32gui
import win32con
import ctypes
from ctypes import wintypes


def bring_to_front(hwvn):
    user32 = ctypes.WinDLL("user32")
    user32.SetWindowPos.restype = wintypes.HWND
    user32.SetWindowPos.argtypes = [wintypes.HWND, wintypes.HWND, wintypes.INT, wintypes.INT, wintypes.INT,
                                    wintypes.INT,
                                    wintypes.UINT]

    user32.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, 0x0001)
    win32gui.SetActiveWindow(hwnd)

def onMouse(event, x, y, flags, param):
    global clicked
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True


cap = cv2.VideoCapture('E:\\kvn\\git\\show_movie_py\\video.mp4 ')
cv2.namedWindow("window8march", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("window8march",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_OPENGL)

hwnd = win32gui.FindWindow(None, 'window8march')

clicked = False

cv2.setMouseCallback('window8march', onMouse)
success, frame = cap.read()
cv2.setWindowProperty("window8march", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while (cv2.waitKey(1) != 27):

    if frame is not None:
        cv2.imshow('window8march', frame)
    else:
        cap = cv2.VideoCapture('video.mp4')
    success, frame = cap.read()
    bring_to_front(hwnd)

cap.release()
cv2.destroyAllWindows()