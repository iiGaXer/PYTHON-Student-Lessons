import random
from time import sleep
from os import system 
import sys

system("cls")

username = input("What is your name?\n")
current_year = int(input("Current year?\n"))
date_birth = int(input("Date of birth?\n"))

Age = current_year - date_birth
print(username + '\'s', "age:", Age)