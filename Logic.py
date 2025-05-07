# if = Do Some Code Only IF Some Condition Is True
#      else Do Something ELSE

Age = int(input("Enter Your Age : "))

if Age >= 100 :
    print("You Are Too Old To Sign Up")
elif Age >= 18 :
    print("You Are Now Signed Up!")
elif Age < 0 :
    print("You Haven't Been Born Yet!")
else :
    print("You Must Be 18+ To Sign Up")

# ==========================================================
print()
Response = input("Would You Like Food? (Y/N) : ")

if Response == "Y" :
    print("Have Some Food!")
else :
    print("No Food For You!")

# ==========================================================
print()
Name = input("Enter Your Name : ")

if Name == "" :
    print("You Did Not Type In Your Name!")
else :
    print(f"Hello {Name}")

# ==========================================================
print()
For_Sale = True
Online = False

if For_Sale :
    print("This Item Is For_Sale")
else :
    print("This Item Is Not For_Sale")

if Online :
    print("This User Is Online")
else :
    print("This User Is Offline")