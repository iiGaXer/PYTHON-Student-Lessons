import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    x = min(arr)
    y = max(arr)

    mini = 0
    maxi = 0

    arr.remove(min(arr))

    for i in range(len(arr)):
        maxi += arr[i]

    arr.append(x)
    arr.remove(max(arr))

    for i in range(len(arr)):
        mini += arr[i]

    print(mini, maxi)
    


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
