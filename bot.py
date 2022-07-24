from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# row 1: x = 1330 y = 590
# row 2: x = 1400 y = 590
# row 3: x = 1490 y = 590
# row 4: x = 1560 y = 590


def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(1270, 580)[0] == 0:
        click(1270,590)
    if pyautogui.pixel(1400, 580)[0] == 0:
        click(1400, 590)
    if pyautogui.pixel(1540, 580)[0] == 0:
        click(1540, 590)
    if pyautogui.pixel(1660, 580)[0] == 0:
        click(1660, 590)
        
