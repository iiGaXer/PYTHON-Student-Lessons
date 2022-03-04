from time import sleep
import sys
import getpass

print("Hello " + getpass.getuser())

x = "Mom"
y = 1234567890

#! 3rd Method
print(f"x is{x: >8}, y is {y:.2f}")

#? 1st Method
print("x is {}, y is {}".format(x, y))

#* 2nd Method
print("x is {: >8}, y is {:.2f}".format(x,y))