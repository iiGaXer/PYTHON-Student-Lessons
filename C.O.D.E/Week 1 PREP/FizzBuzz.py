import math
import os
import random
import re
import sys

def fizzBuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print(f"FizzBuzz")
        
        elif i % 3 == 0 and i % 5 != 0:
            print(f"Fizz")
            
        elif i % 5 == 0 and i % 3 != 0:
            print(f"Buzz")
            
        elif i % 3 != 0 and i % 5 != 0:
            print(i)
            
        
        
if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
