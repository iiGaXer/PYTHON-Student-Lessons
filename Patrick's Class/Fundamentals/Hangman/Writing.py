from time import sleep
import random
import requests
import sys
from random import randint

def writing():
    with open("file.txt", "w") as w_file:
        w_file.write("Hello World!\n")
        w_file.write("Hello World!")