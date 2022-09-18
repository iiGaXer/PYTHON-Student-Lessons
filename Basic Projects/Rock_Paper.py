import random
from time import sleep
from os import system 
import sys

system("cls")
Choice = ["Rock", "Paper", "Scissors"]
Scores = [0, 0]
Points = [0, 0]

def Choices(x):
    for i in range(x):
            system("cls")
            print(f"Chose: Rock, Paper, or Scissors?")
            person = input()
            pc = random.choice(Choice)

            if person == 'Rock' and pc == 'Paper':
                sleep(1)
                print(f"You lost! AI:", pc, ">", person)
                Points[1] += 1
                sleep(10)

            elif person == 'Paper' and pc == 'Rock':
                sleep(1)
                print(f"You won! You:", person, ">", pc)
                Points[0] += 1
                sleep(10)

            elif person == 'Paper' and pc == 'Scissors':
                sleep(1)
                print(f"You lost! AI:", pc, ">", person)
                Points[1] += 1
                sleep(10)

            elif person == 'Scissors' and pc == 'Paper':
                sleep(1)
                print(f"You won! You:", person, ">", pc)
                Points[0] += 1
                sleep(10)

            elif person == 'Rock' and pc == 'Scissors':
                sleep(1)
                print(f"You won! You:", person, ">", pc)
                Points[0] += 1
                sleep(10)

            elif person == 'Scissors' and pc == 'Rock':
                sleep(1)
                print(f"You lost! AI:", pc, ">", person)
                Points[1] += 1
                sleep(10)

            elif person == pc:
                sleep(1)
                print(f"Tie! Results:", pc, "=", person)
                sleep(10)
                i -= 1

def score():
    Scores[0] = Points[0]
    Scores[1] = Points[1]
    print(f"\n")
    print(f"Score is:", Scores[0], ":", Scores[1])

def Ending():
    print("Finished! Game has ended: Wanna try again?")
    option = input()
    if option == "Yes" or "yes":
        pass
    else:
        sys.exit("You exited the game.")

print(f"Welcome! What is your name?")
Player = input()
print(f"Hello %s!" % Player)
sleep(4.3)
system("cls")


print(f"Welcome to Rock, Paper, Scissors!")
sleep(1)
print(f"Let's Play!")
sleep(1.1)

while True:
    print(f"How many rounds?")
    Rounds = int(input())
    sleep(3)
    system("cls")
    print(f"Let's play", Rounds, "rounds!")
    sleep(2.3)
    Choices(Rounds)
    score()
    Ending()
    Scores = [0, 0]
    Points = [0, 0]



