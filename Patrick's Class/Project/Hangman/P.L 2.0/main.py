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

    with open("Words.txt", "w") as w_file:
        w_file.write(str(Game_number))

    # with open("Words.txt", "r") as r_file:
    #     print("_ "*len(Game_number))
    
    with open("Words.txt", "w") as w_file:
        for word in WORDLIST:
            w_file.write(word + '\n')

    while len(Game_number) < 3:
        Game_number = WORDLIST[random_num]
        
    print(Game_number)

def The_word():
    with open("Words.txt", "r") as r_file:
        for line in r_file:
            print(line)

index()