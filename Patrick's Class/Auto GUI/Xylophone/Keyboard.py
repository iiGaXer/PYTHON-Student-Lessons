from time import sleep
import pyautogui
import keyboard
import sys
from Music_Key import Music_1 as Note_1
from Music_Key import Music_2 as Note_2
from Music_Key import B_day as B_day

def Key_pressed():
    if keyboard.read_key() =="o":
        Note_1()

    if keyboard.read_key() == "i":
        Note_2()

    if keyboard.read_key() == "u":
        B_day()

    if keyboard.read_key() == "p":
        sys.exit()
        