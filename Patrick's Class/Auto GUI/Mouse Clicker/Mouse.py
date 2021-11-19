from time import sleep
import pyautogui
import keyboard
import sys
from Choices import Choices as Choice


def Mouse_coordinates():
    while True:
        if keyboard.read_key() == "r":
            print(pyautogui.size())
            break


        if keyboard.read_key() == "f":  
            print(pyautogui.position())
            break

def Clicks():
    while True:
        if keyboard.read_key() == "e":
            print(f"Are you ready to start the Auto-clicker? (Press e again to start, press q to exit.)")
            Choice()
            break

        if keyboard.read_key() == "q":
            sys.exit()

