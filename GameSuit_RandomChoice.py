# Game Suit Japan (Rock, Paper, Scissors)
import random

print()
Options = ("Rock", "Paper", "Scissors")
Options1 = ("Rock", "Paper", "Scissors")
Player = None
Player1 = None
Computer = random.choice(Options)
Computer1 = random.choice(Options1)

# --------------------------------------------------------------
Player = input("Enter A Choice (Rock, Paper, Scissors) : ")

print(f"Player : {Player}")
print(f"Computer : {Computer}")

# --------------------------------------------------------------
print()
while Player1 not in Options1 :
    Player1 = input("Enter A Choice (Rock, Paper, Scissor) : ")

print(f"Player1 : {Player1}")
print(f"Computer1 : {Computer1}")

if Player1 == Computer1 :
    print("It's A Tie!")
elif Player1 == "Rock" and Computer1 == "Scissors" :
    print("You Win!")
elif Player1 == "Paper" and Computer1 == "Rock" :
    print("You Win!")
elif Player1 == "Scissors" and Computer1 == "Paper" :
    print("You Win!")
else :
    print("You Lose!")

#----------------------------------------------------------------
print()
Options2 = ("Rock", "Paper", "Scissors")
Running = True

while Running :
    Player2 = None
    Computer2 = random.choice(Options2)

    while Player2 not in Options2 :
        Player2 = input("Enter A Choice (Rock, Paper, Scissor) : ")

    print(f"Player2 : {Player2}")
    print(f"Computer2 : {Computer2}")

    if Player2 == Computer2:
        print("It's A Tie!")
    elif Player2 == "Rock" and Computer2 == "Scissors":
        print("You Win!")
    elif Player2 == "Paper" and Computer2 == "Rock":
        print("You Win!")
    elif Player2 == "Scissors" and Computer2 == "Paper":
        print("You Win!")
    else:
        print("You Lose!")

    # Play_Again = input("Play Again? (Y/N) : ").upper()   # Jika (y/n) maka ("Play Again? (y/n) : ").lower() | OR
    # if not Play_Again == "Y" :                           #                                                  | SAMA DENGAN
        # Running = False                                  #                                                  | DIBAWAH

    if not input("Play Again? (Y/N) : ").upper() == "Y" :     # Jika ("Play Again? (y/n)").lower() == "y" :
        Running = False

print()
print("Thanks For Playing!")