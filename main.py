import cv2
import win32gui
import win32con
import ctypes
from ctypes import wintypes


def bring_to_front(hwnd):
    user32 = ctypes.WinDLL("user32")
    user32.SetWindowPos.restype = wintypes.HWND
    user32.SetWindowPos.argtypes = [wintypes.HWND, wintypes.HWND, wintypes.INT, wintypes.INT, wintypes.INT,
                                    wintypes.INT,
                                    wintypes.UINT]

    user32.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, 0x0001)
    win32gui.SetActiveWindow(hwnd)


wndname = "window8march"
filename = '\\\\srv1-dc\\NETLOGON\\video.mp4'
#filename = "E:\\video\\2021-03-04 11-18-05.mkv"
cap = cv2.VideoCapture(filename)
cv2.namedWindow(wndname, cv2.WND_PROP_FULLSCREEN)
HWND = win32gui.FindWindow(None, wndname)
success, frame = cap.read()
cv2.setWindowProperty(wndname, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while cv2.waitKey(1) != 27:

    if frame is not None:
        cv2.imshow(wndname, frame)
    else:
        #cap = cv2.VideoCapture(filename)
        cap = cv2.VideoCapture('\\\\srv1-dc\\NETLOGON\\video1.mp4')
    success, frame = cap.read()
    bring_to_front(HWND)

cap.release()
cv2.destroyAllWindows()
