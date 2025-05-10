# Function = A Block Of Reusable Code
#            Place () After The Function Name To Invoke It

#---------------------------------------------------------
print()
print("Happy Birthday To You!")
print("You Are Old!")
print("Happy Birthday To You!")
print()
print("Happy Birthday To You!")
print("You Are Old!")
print("Happy Birthday To You!")
print()
print("Happy Birthday To You!")
print("You Are Old!")
print("Happy Birthday To You!")
print()

#---------------------------------------------------------
print("======================")
def Happy_Birthday () :
    print("Happy Birthday To You!")
    print("You Are Old!")
    print("Happy Birthday To You!")
    print()

Happy_Birthday()
Happy_Birthday()
Happy_Birthday()

#---------------------------------------------------------
print("======================")
def Happy_Birthday (Name) :
    print(f"Happy Birthday To {Name}!")
    print("You Are Old!")
    print("Happy Birthday To You!")
    print()

Happy_Birthday("Kadal")
Happy_Birthday("Mesir")
Happy_Birthday("Kunam")

#---------------------------------------------------------
print("======================")
def Happy_Birthday (Name, Age) :
    print(f"Happy Birthday To {Name}!")
    print(f"You Are {Age} Years Old!")
    print("Happy Birthday To You!")
    print()

Happy_Birthday("Kadal", 20)
Happy_Birthday("Mesir", 30)
Happy_Birthday("Kunam", 40)

# OR
print("======================")
def Happy_Birthday (Age, Name) :
    print(f"Happy Birthday To {Name}!")
    print(f"You Are {Age} Years Old!")
    print("Happy Birthday To You!")
    print()

Happy_Birthday("Kadal", 20)
Happy_Birthday("Mesir", 30)
Happy_Birthday("Kunam", 40)

# Example Progam
print("======================")
def Display_Invoice (Username, Amount, Due_Date) :
    print(f"Hello {Username}")
    print(f"Your Bill Of ${Amount : .2f} Is Due : {Due_Date}")
    print()

Display_Invoice("Kadal", 42.40, "02/02")
Display_Invoice("Kadal", 102.40, "05/05")
