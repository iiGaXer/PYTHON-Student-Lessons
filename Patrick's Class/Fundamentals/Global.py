from time import sleep
import sys

a = 17

def function():
    global a
    a = 23
    print(2, a)

print(1, a)
function()
print(3, a)

