import numpy as np
import cv2
import os
import win32gui
import win32con
import ctypes
from ctypes import wintypes


def bring_to_front(self, new=True):
    """Bring a window into focus.
    Kept the old way just to be on the safe side.
    """
    if new:
        win32gui.ShowWindow(self.hwnd, True)
    else:
        self.restore()

    # Sometimes it seems to fail but then work a second time
    try:
        win32gui.SetForegroundWindow(self.hwnd)
    except pywintypes.error:
        time.sleep(0.5)
        win32gui.ShowWindow(self.hwnd, True)
        try:
            win32gui.SetForegroundWindow(self.hwnd)
        except pywintypes.error:
            pass

cap = cv2.VideoCapture('E:\\kvn\\git\\show_movie_py\\video.mp4 ')
cv2.namedWindow("window8march", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("window8march",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_OPENGL)

clicked = False
def onMouse(event, x, y, flags, param):
    global clicked
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True


cv2.setMouseCallback('window8march', onMouse)
success, frame = cap.read()

#hwnd = win32gui.GetForegroundWindow()
#win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 600, 300, 0, 0, win32con.SWP_NOSIZE)

hwnd = win32gui.FindWindow(None, 'window8march')
win32gui.ShowWindow(hwnd, True)
#win32gui.(hwnd, 5)
win32gui.SetForegroundWindow(hwnd)

# user32 = ctypes.WinDLL("user32")
# user32.SetWindowPos.restype = wintypes.HWND
# user32.SetWindowPos.argtypes = [wintypes.HWND, wintypes.HWND, wintypes.INT, wintypes.INT, wintypes.INT, wintypes.INT,
#                                 wintypes.UINT]
#
# user32.SetWindowPos(hwnd, -1, 600, 300, 0, 0, 0x0001)

firstrun = False
while (cv2.waitKey(1) != 27):
    # if firstrun:
    #     cv2.setWindowProperty("window", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    #     cv2.setWindowProperty("window", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)
    #     cv2.setWindowProperty("window", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    #     firstrun = False
    if frame is not None:
        cv2.imshow('window8march', frame)
    else:
        cap = cv2.VideoCapture('video.mp4')
    success, frame = cap.read()
#    cv2.setWindowProperty("window8march",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    hwnd = win32gui.FindWindow(None,'window8march')
    user32 = ctypes.WinDLL("user32")
    user32.SetWindowPos.restype = wintypes.HWND
    user32.SetWindowPos.argtypes = [wintypes.HWND, wintypes.HWND, wintypes.INT, wintypes.INT, wintypes.INT, wintypes.INT,
                                     wintypes.UINT]

    user32.SetWindowPos(hwnd, -1, 0, 0, 0, 0, 0x0001)
    #hwnd = win32gui.GetForegroundWindow()

    #win32gui.SetFocus(hwnd)
    # try:
    #win32gui.SetForegroundWindow(hwnd)
    win32gui.SetActiveWindow(hwnd)
    # except:
    #     d-1

cap.release()
cv2.destroyAllWindows()