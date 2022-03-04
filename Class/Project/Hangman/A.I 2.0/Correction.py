import sys
from time import sleep
from Word import index as word
import keyboard
import requests
from os import system

def hangman():
        print("   _____ \n"
                "  |     | \n"
                "  |     |\n"
                "  |     | \n"
                "  |     O \n"
                "  |    /|\ \n"
                "  |    / \ \n"
                "__|__\n")

def hangman_3():
        print("   _____ \n"
                "  |     O \n"
                "  |    /|\ \n"
                "  |    / \ \n"
                "__|__\n")

def main():
    i = 0
    guesser_word = []
    words = []
    hangman()
    word()
    with open("Words.txt", "r") as r_file:
        line = str(r_file.readline())
        number = len(line)

    value = []

    for a in range(len(line)):
        guesser_word.append("_")

    lives = number
    Comparrision = 0
    # splittered = line

    # def difference(x) {
    #     global guesser_word
    #     global Comparrision
    #     if guesser_word[x] == line[x]:
    #         Comparrision = True
    #     else:
    #         Comparrision = False
    # }
    a = 0

    while Comparrision != True or False:
        # substring_line = line[i:i+1]
        if len(value) == len(line):
            for j in range(number):
                if guesser_word[j] == line[j]:
                    Comparrision = True
                    a += 1
                    break
                else:
                    Comparrision = False
                    a -= 1
                    break
        
        if a >= 1:
            break
        elif a <= -1:
            break
        elif a == 0:
            pass

        wrong_or_right = False

        print("\n")
        guesser = input()
        for i in range(number):

                if guesser == line[i]:
                    guesser_word[i] = guesser
                    value.append(guesser)

                    system("cls")
                    hangman()

                    # for i in range(len(guesser_word) - 1):
                    #     print(guesser_word[i], end=f" ")

                    for character in guesser_word:
                        print(character, end=f" ")
                        
                    wrong_or_right = True
                    break

        if not wrong_or_right:
            system("cls")
            print("Wrong! It is not " + guesser)
            print(lives, "lives left")
            lives -= 1
            sleep(3)


            if lives == 0:
                print(" \nSorry! Ran out of lives! This is the word:")
                hangman_3()
                print(line)
                sys.exit()

            elif lives != 0:
                system("cls")
                hangman()
                for character in guesser_word:
                    print(character, end=f" ")
                pass
            else:
                system("cls")
                hangman()
                for character in guesser_word:
                    print(character, end=f" ")
                pass



    if Comparrision == True:
        print(f"\nYou did it! You got the word:")
        sleep(1.3)

        for item in line:
            print(item, end="")

    elif Comparrision == False:
        print(" \nSorry! Ran out of lives! This is the word:")
        sleep(1.3)
        hangman()
        print(line)

    

            

