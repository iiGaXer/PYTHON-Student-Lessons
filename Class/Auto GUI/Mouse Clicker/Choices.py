import keyboard
import pyautogui
import sys

def Choices():
    if keyboard.read_key() == "e":
        pyautogui.click(clicks = 100)
    if keyboard.read_key() == "q":
        sys.exit()

