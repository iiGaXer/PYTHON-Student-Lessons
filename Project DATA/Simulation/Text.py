import os
import time
import random
from time import sleep
import turtle

# def choice():

def Intro():
    Welcome_message = [". . .", "Are you..?", "I don't know what or who you are"]
    After_message = ["It doesn't matter anyways. . .", "Nevermind. . ."]
    Welcome_Gen = random.randint(0, 2)
    After_Gene = random.randint(0, 1)

    print(Welcome_message[Welcome_Gen])
    sleep(5)
    print(After_message[After_Gene])
    sleep(3)
    print(f"What matters now is that you are here.")
    sleep(3)
    print("And now, we can finally begin.")
    input()
    sleep(4)
    print(f"Yo◆r cho□ces do■'t ma⧫⧫er")
    sleep(10)
    print(f"This is your body.")
    sleep(1.5)
    print(f"For now, it has materialized.")
    sleep(1.3)
    print(f"I wonder...")
    sleep(2)
    print(f"How life will be in this world... =)")

def Main():
    sleep(2)
    print(f" * Everything is white...")
    sleep(1)
    print(f" * I remember that I am a...")
