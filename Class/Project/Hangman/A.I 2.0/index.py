import sys
from time import sleep
from Correction import main as index
from os import system

system("cls")
print(f"Hello! Let's play Hangman!")
sleep(1.4)
print(f"The goal of the game is simple! Just guess the word!")
sleep(2.2)
print(f"Lets start!")
sleep(2.2)
print(f"Please guess this word!")

with open("Word_current.txt", "w") as w_file:
        w_file.write("")

index()

Response = ""

while True:
        Response = input("\nWanna play again?\n")
        if Response != 'No' or Response != 'no':
                break
        index()

sys.exit()