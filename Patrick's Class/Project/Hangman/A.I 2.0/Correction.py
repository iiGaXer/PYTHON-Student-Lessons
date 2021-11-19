import sys
from time import sleep
from Word import index as word
import keyboard
import requests

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
    hangman()
    print(f"Lets start!")
    print(f"Please guess this word!")
    word()
    with open("Words.txt", "r") as r_file:
        line = str(r_file.readline())
        number = len(line)

    lives = number

    while i != number:
        substring_line = line[i:i+1]
        guesser = input()
        if guesser in line:
            # print("\n" + guesser + " _ "*(number - (i + 1)))
            splitter = line.split(guesser)
            word_split = splitter[0]
            word_split2 = splitter[1]

            value_split = len(word_split)
            value_split2 = len(word_split2)

            guesser_string = str(guesser)
            i += 1
            # guesser_word.append(guesser)
            with open("Word_current.txt", "a") as a_file:
                if value_split == 0:
                    a_file.write(str(guesser + " "))
                else:
                    guesser_word.insert(i, guesser)
                    a_file.write(str(guesser_word))
            with open("Word_current.txt", "r") as r_file:
                words = str(r_file.readline())
                value_words = len(words)
            
            hangman()
            if value_split == 0:
                print(words + "_ "*(number - i))
            else:
                print((value_split)*" _" + words + "_ "*(value_split2))#number - (i - 1)))

        else:
            print("Wrong! It is not " + guesser)
            print(lives, "lives left")
            lives -= 1


            if lives == 0:
                print(" \nSorry! Ran out of lives! This is the word:")
                hangman()
                print(line)
                sys.exit()

            elif lives != 0:
                pass
            else:
                pass
            

