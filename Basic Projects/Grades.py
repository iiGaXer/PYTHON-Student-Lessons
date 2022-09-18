import random
from time import sleep
from os import system 
import sys

def Number(x, num_min, num_max):
    for i in range(num_min, num_max):
        x.append(i)

system("cls")

user_grade = int(input('What is your grade? (Must be a number between 0-100)\n'))

A = []
B = []
C = []
D = []
F = []

Number(A, 80, 101)
Number(B, 70, 80)
Number(C, 60, 70)
Number(D, 50, 59)
Number(F, 0, 50)

for i in range(len(A)):
    if (user_grade == A[i]):
        if (100 >= user_grade >= 90):
            print("Your grade is A+!")
            break
        
        elif (89 >= user_grade >= 85):
            print("Your grade is A!")
            break
        
        elif (84 >= user_grade >= 80):
            print("Your grade is A-!")
            break

    else:
        pass

for i in range(len(B)):
    if (user_grade == B[i]):
        if (79 >= user_grade >= 77):
            print("Your grade is B+!")
            break
        
        elif (76 >= user_grade >= 73):
            print("Your grade is B!")
            break
        
        elif (72 >= user_grade >= 70):
            print("Your grade is B-!")
            break

    else:
        pass

for i in range(len(C)):
    if (user_grade == C[i]):
        if (69 >= user_grade >= 67):
            print("Your grade is C+!")
            break
        
        elif (66 >= user_grade >= 63):
            print("Your grade is C!")
            break
        
        elif (62 >= user_grade >= 60):
            print("Your grade is C-!")
            break

    else:
        pass

for i in range(len(D)):
    if (user_grade == D[i]):
        if (59 >= user_grade >= 57):
            print("Your grade is D+!")
            break
        
        elif (56 >= user_grade >= 53):
            print("Your grade is D!")
            break
        
        elif (52 >= user_grade >= 50):
            print("Your grade is D-!")
            break

    else:
        pass

for i in range(len(F)):
    if (user_grade == F[i]):
        if (49 >= user_grade >= 0):
            print("Your grade is F!")

    else:
        pass

