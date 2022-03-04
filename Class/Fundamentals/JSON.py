import sys
from time import sleep
from os import system

#! JSON is nested Lists and Dictionaries
#? It is a text for storing and exchanging data.

def challenge():
    peoples = [
        {
            "Name":"John",
            "City":"Ottawa",
            "Age":30
        },
        {
            "Name":"Smith",
            "City":"Toronto",
            "Age":31
        }
    ]


    for people in peoples:
        for key in people:
            print(key, ":", people[key])

        print('\n') 

challenge()

