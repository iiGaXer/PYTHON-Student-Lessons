from time import sleep
import getpass
from random import randint, uniform
from os import system 
import keyboard
import numpy as np
import time
import sys


system("cls")

class Game:
    def __init__(self, username):
        self.user = username

    def Introduction(self):
        print("Hello! Welcome to Countdown!")
        sleep(2)
        print("I see that your username is", self.user, "!")

        while True:
            choice = input("\nDo you want to change it? (Yes/yes) or (No/no)?\n")
            sleep(1)

            if choice == 'yes' or choice == 'Yes':
                self.name = input("Great! What is your name then?\n")
                sleep(2)
                print(self.name, "Huh? Great name!")
                break
            
            elif choice == 'no' or choice == 'No':
                print("Alright", self.user, "!")
                break
            else:
                print("I didn't understand what you said and therefore re-iterate this program!")

        print("\nLet's start!")
        sleep(1)
        print("Remember to press the r key when the countdown stops!")
        sleep(4)
    
    def Convert_time(self, sec):
        self.mins = sec // 60
        self.sec = sec % 60
        self.hours = self.mins // 60
        self.mins = sec % 60
        print("Your time = {0}:{1}:{2}".format(int(self.hours), int(self.mins), self.sec))

    def countdown(self):
        self.max = uniform(0, 100.00)
        self.count = uniform(0, 2.00)
        self.timer = 0

        if self.max == 0:
            self.max = uniform(0, 200.00)
            self.min = uniform(0, self.max)

        for i in np.arange(0, self.max, self.count):
            print(i)
            sleep(.0001)
        
        self.start = time.time()

        while True:
            if keyboard.is_pressed('r'):
                self.end = time.time()
                break
            else:
                pass

        self.time = self.end - self.start
        self.Convert_time(self.time)
        self.time = "{0}:{1}:{2}".format(int(self.hours), int(self.mins), int(self.sec))

    def End(Self):
        sleep(1)
        Round = input("Would you like to try again? (Yes/yes) or (No/no)?\n")
        if Round == "Yes" or Round == "yes":
            pass
        elif Round == "No" or Round == "no":
            sleep(.5)
            print("Bye/Au-revoir/Ciao!")
            sys.exit()

        else:
            sleep(.5)
            print("Bye/Au-revoir/Ciao!")
            sys.exit()
    

game = Game(getpass.getuser())
game.Introduction()

while True:
    game.countdown()
    game.End()
    sleep(1)