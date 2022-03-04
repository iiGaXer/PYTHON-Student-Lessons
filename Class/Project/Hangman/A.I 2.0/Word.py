import random
import sys
from time import sleep
import requests
from random import randint
# import choice

def index():
    site = 'https://www.mit.edu/~ecprice/wordlist.10000'
    # i = 0
    request = requests.get(site)
    WORDLIST = request.text.splitlines()
    random_num = randint(0, len(WORDLIST) - 1)
    number = len(WORDLIST[random_num])
    Game_number = WORDLIST[random_num]

    j = 0

    while len(Game_number) < 3 :
        Game_number = WORDLIST[random_num]
        #? for i in range(len(Game_number)):
        # ?    if (Game_number[j] != Game_number[i]):
        #  ?       j += 1
        #   ?      Game_number[j] = Game_number[i]
        #? j += 1
        #? Game_number = Game_number[:j]

    # for word in Game_number:
    #     if ha:
    #         Game_number = WORDLIST[random_num]
    
    # letters = Game_number
    # for i in range(len(Game_number)):
        # if i != len(Game_number):
    #     for j in range(len(Game_number) - 1):
                # if j != len(Game_number):
    #         if letters[i] == Game_number[j + 1]:
    #             Game_number = WORDLIST[random_num]
    #             break
    #         else:
    #             pass
        #                 i = len(Game_number)
        #                 j = len(Game_number)
        #                 break
        #         else:
        #             break
        # else:
        #     break
                

    # for index in range(len(Game_number)):
    #     print(Game_number[index])


    with open("Words.txt", "w") as w_file:
        w_file.write(Game_number)
    
    with open("Words.txt", "r") as r_file:
        print("_ "*len(Game_number))

def The_word():
    with open("Words.txt", "r") as r_file:
        for line in r_file:
            print(line)

