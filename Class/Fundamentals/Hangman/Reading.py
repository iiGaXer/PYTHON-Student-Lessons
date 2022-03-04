from time import sleep
import random
import requests
import sys
from random import randint

def reading():
    with open("file.txt", "r") as r_file:
        for line in r_file:
            print(line)

        # print(r_file.readlines())
