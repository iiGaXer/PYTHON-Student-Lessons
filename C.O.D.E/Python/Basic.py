import math
import random
import sys

def printing():
    """Challenge 1: Printing"""
    print(f"Hello, World!")

def if_else():
    """Challenge 2: If and Else"""
    n = input()

    if n % 2 != 0:
        print(f"Weird")
    
    elif n % 2 == 0 and n >= 2 and n <= 5:
        print(f"Not Weird")

    elif n % 2 == 0 and n >= 6 and n <= 20:
        print(f"Weird")

    elif n % 2 == 0 and n > 20:
        print(f"Not Weird")

def arithmetic_operators():
    """Challenge 3: Arithmetic Operators"""
    a = int(input())
    b = int(input())        

    print(a + b)
    print(a - b)
    print(a * b)

def arithmetic_operators_2():
    """Challenge 4: 2nd Arithmetic Operators"""
    a = int(input())
    b = int(input()) 

    print(a//b)
    print(a/b)

def loops():
    """Challenge 5: For-Loops"""
    n = int(input())

    for i in range(n):
        print(i * i)

def function():
    """Challenge 6: Function"""
    def is_leap(year):
        leap = False
        
        if year % 4 == 0:
            if year % 100 != 0 or year % 400 == 0:
                    leap = True
        
        else:
            pass       
        
        return leap
    
    year = int(input())
    print(is_leap(year))

def print_function():
    """Challenge 7"""
    if __name__ == '__main__':
        n = int(input())
        
        lists = []
        
        for i in range(n + 1):
            lists.append(i)
        
        for i in range(len(lists) - 1):
            print(lists[i + 1], end = "")

