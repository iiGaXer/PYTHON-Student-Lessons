from time import sleep
import random
import requests
import sys
from random import randint

site = 'https://www.mit.edu/~ecprice/wordlist.10000'
request = requests.get(site)
WORDLIST = request.text.splitlines()
random_num = randint(0, len(WORDLIST))
number = len(WORDLIST)
Game_number = WORDLIST[random_num]
# print(str(Game_number))

def words_hangman():
    global Game_number
    global WORDLIST
    with open("Word.txt", "w") as w_file:
        w_file.write(str(WORDLIST))
    
    with open("Word.txt", "r") as r_file:
        for line in r_file:
            print(line)



    
words_hangman()
    