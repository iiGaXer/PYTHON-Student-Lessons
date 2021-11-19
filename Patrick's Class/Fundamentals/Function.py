import sys
from time import sleep

def passable():
    pass

def main():
    print(f"Hello~!")

passable()
main()

def dummy_function(str, str2):
    print(str + " " + str2)

dummy_function("lloll", "a")

def d_f2(str, str2, str3="lisa"):
    print("First child is " + str3)

d_f2(str="alvin", str2="lolls")
d_f2(str="alvin", str2="lolls2", str3="Linda")

def num_function(x):
    return 5*x

y = num_function(x=3)
print(y)
