# Python Number Guessing Game

import random

print()
Lowest_Num = 1
Highest_Num = 100

Answer = random.randint(Lowest_Num, Highest_Num)

Guesses = 0
Is_Running = True

print(Answer)
print()
print("Python Number Guessing Game")
print(f"Select A Number Between {Lowest_Num} and {Highest_Num}")

# while Is_Running :
    # Guess = input("Enter Your Guess : ")
    # if Guess.isdigit() :
        # pass
    # else :
        # print("Invalid Guess")
        # print(f"Please Select A Number Between {Lowest_Num} and {Highest_Num}")

print()
while Is_Running :
    Guess = input("Enter Your Guess : ")
    if Guess.isdigit() :
        Guess = int(Guess)
        Guesses += 1
        if Guess < Lowest_Num or Guess > Highest_Num :
            print("That Number Is Out Of Range")
            print(f"Please Select A Number Between {Lowest_Num} and {Highest_Num}!")
        elif Guess < Answer :
            print("Too Low! Try Again!")
        elif Guess > Answer:
            print("Too High! Try Again!")
        else :
            print(f"CORRECT! The Answer Was {Answer}")
            print(f"Number Of Guesses : {Guesses}")
            Is_Running = False
    else :
        print("Invalid Guess")
        print(f"Please Select A Number Between {Lowest_Num} and {Highest_Num}")