import random
from time import sleep
from os import system 
import sys

system("cls")
Choices = ["Rock", "Paper", "Scissors"]
Scores = [0, 0]
Points = [0, 0]
AI = random.choice(Choices)

class Game:

    '''
    A Rock, Paper, and Scissors game.

    !Everything here is IMPORTANT
    '''

    def __init__(self, pc, scored = Scores, points = Points):
        self.pc = pc
        self.scored = scored
        self.points = points

    def Entrance():
        print(f"Welcome to Rock, Paper, Scissors!")
        sleep(1)
        print(f"Let's Play!")
        sleep(0.5)

    def Cont(x):
        system("cls")
        print(f"Let's play", x, "rounds!")
        print(f"Chose: Rock, Paper, or Scissors?")

    def Choices(self, x):
        for i in range(x):
            self.person = input()
            self.pc = self.pc
            if self.person == "rock" or "Rock" and self.pc == "Paper" or "paper":
                sleep(1)
                print(f"You lost! AI:", self.pc, ">", self.person)
                self.points[1] += 1

            elif self.person == "Paper" or "paper" and self.pc == "rock" or "Rock":
                sleep(1)
                print(f"You won! You:", self.person, ">", self.pc)
                self.points[0] += 1

            elif self.person == "Paper" or "paper" and self.pc == "Scissors" or "scissors":
                sleep(1)
                print(f"You lost! AI:", self.pc, ">", self.person)
                self.points[1] += 1

            elif self.person == "Scissors" or "scissors" and self.pc == "Paper" or "paper":
                sleep(1)
                print(f"You won! You:", self.person, ">", self.pc)
                self.points[0] += 1

            elif self.person == "rock" or "Rock" and self.pc == "Scissors" or "scissors":
                sleep(1)
                print(f"You won! You:", self.person, ">", self.pc)
                self.points[0] += 1

            elif self.person == "Scissors" or "scissors" and self.pc == "rock" or "Rock":
                sleep(1)
                print(f"You lost! AI:", self.pc, ">", self.person)
                self.points[1] += 1

    def score(self):
        self.scored[0] = self.points[0]
        self.scored[1] = self.points[1]
        print(f"\n")
        print(f"Score is:", self.scored[0], ":", self.scored[1])

    def Ending():
        print("Finished! Game has ended: Wanna try again?")
        option = input()
        if option == "Yes" or "yes":
            pass
        else:
            sys.exit("You exited the game.")


print(f"Welcome! What is your name?")
Player = input()
print(f"Hello", Player)
Games = Game(AI)

while True:
    Game.Entrance()

    print(f"How many rounds?")

    Rounds = int(input())
    Game.Cont(Rounds)
    Game.Choices(Rounds)
    Game.score()
    Game.Ending()
