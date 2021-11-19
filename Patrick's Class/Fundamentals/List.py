import sys
from time import sleep

fruits = ["apple", "bannana", "cherry"]

Fruits_2_0 = []

def print_list(x):
    for i in range(len(x)):
        print(x[i], "\n")

def print_list_2(x):
    for fruit in fruits:
        print(fruit)

def list_actions():
    fruits.pop()

    print_list(fruits)

    fruits.remove("apple")

    print_list(fruits)

def list_data(x):
    Fruits_2_0 = x.copy()
    print(print_list(Fruits_2_0))

def challenge():
    for i in range(9, 0, -2):
        print(i)

def ascending_descending():
    fruits = [1, 2, 7, 8, 0]

    fruits.sort()
    print(print_list(fruits))

    sleep(1)

    fruits.sort(reverse = True)
    print(print_list(fruits))

    sleep(1)

    Fruits_2_0 = sorted(fruits)
    print(print_list(Fruits_2_0))

    sleep(1)

    Fruits_2_0 = sorted(Fruits_2_0, reverse=True)
    print(print_list(Fruits_2_0))

