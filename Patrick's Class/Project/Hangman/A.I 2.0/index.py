import sys
from time import sleep
from Correction import main as index

print(f"Hello! Let's play Hangman!")
sleep(1.4)
print(f"The goal of the game is simple! Just guess the word!")
sleep(2.2)

with open("Word_current.txt", "w") as w_file:
        w_file.write("")

index()