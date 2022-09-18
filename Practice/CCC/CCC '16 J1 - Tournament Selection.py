import time
import os
from time import sleep
import random

Win_or_lose_counter = 0

for i in range(6):
    Win_or_lose = input()

    if Win_or_lose == "W":
        Win_or_lose_counter += 1

if (Win_or_lose_counter == 1 or Win_or_lose_counter == 2):
    print(3)

elif (Win_or_lose_counter == 3 or Win_or_lose_counter == 4):
    print(2)

elif (Win_or_lose_counter == 5 or Win_or_lose_counter == 6):
    print(1)

else:
    print(-1)