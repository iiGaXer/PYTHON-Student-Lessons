# from random import randint, uniform
# import numpy as np
# from time import sleep
# import time
# from datetime import datetime

# max = uniform(0, 200.00)
# count = uniform(0, 1.00)

# if max == 0:
#     max = randint(0, 200.00)

# for i in np.arange(0, max, count):
#     print(i)
#     sleep(.0001)

# import time
# from os import system
# import sys

# syntax = 'Welcome'

# def text(msg):
#     for char in msg:
#         sys.stdout.write(char)
#         sys.stdout.flush()

#         if char != "\n":
#             time.sleep(1)

#         else:
#             time.sleep(2)

# system("cls")
# text(syntax)
# from msilib.schema import Font
# from tkinter import font
# import pygame, sys
# from pygame.locals import *

# WINDOW_WIDTH = 500
# WINDOW_HEIGHT = 500

# pygame.init()
# DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# BLACK = (  0,   0,   0)
# WHITE = (255, 255, 255)

# def display_text_animation(string):
#     text = ''
#     for i in range(len(string)):
#         DISPLAYSURF.fill(WHITE)
#         text += string[i]
#         font = pygame.font.SysFont('Courier New', 28)
#         text_surface = font.render(text, True, BLACK)
#         text_rect = text_surface.get_rect()
#         text_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
#         DISPLAYSURF.blit(text_surface, text_rect)
#         pygame.display.update()
#         pygame.time.wait(100)

# def main():
#     while True:
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 sys.exit()

# display_text_animation('Hello World!')
# main()

