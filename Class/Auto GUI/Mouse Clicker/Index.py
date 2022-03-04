from Mouse import Clicks as Click
from Mouse import Mouse_coordinates as Mouse
from time import sleep
from Choices import Choices as Choice
# import pygame

print(f"Welcome to the BETA Auto Clicker! If you wanna see your screen resolution \npress r!")
sleep(1.3)
print(f"If you wanna see your Mouses coordinates every 10 secs, press f!")
sleep(1.3)
print(f"If you wanna start the Clicker, press e!")

# pygame.init()

# background = (10e, 0, 10)

# GUI_x = 300
# GUI_y = 300
# Background = (234, 212, 252)
# Screen = pygame.display.set_mode((GUI_x, GUI_y))
# Screen.fill(Background) 
# pygame.display.flip()


while True:
    Click()
