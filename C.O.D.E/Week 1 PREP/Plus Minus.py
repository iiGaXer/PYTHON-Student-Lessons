import math
import os
import random
import re
import sys


def plusMinus(arr):
    x = 0
    y = 0
    z = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            z += 1
        elif arr[i] >= 1:
            x += 1
        elif arr[i] <= -1:
            y += 1
        else:
            z += 1
    
    x = round(x/len(arr), 6)
    y = round(y/len(arr), 6)
    z = round(z/len(arr), 6)
    
    print(x)
    print(y)
    print(z)
        
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)