import time
import os
from time import sleep
import random

x = int(input())
y = int(input())

# coordinate = [x, y]

if (x > 0 and y > 0):
    print(f"1")

elif (x < 0 and y < 0):
    print(f"3")

elif (x < 0 and y > 0):
    print(f"2")

elif (x > 0 and y < 0):
    print(f"4")