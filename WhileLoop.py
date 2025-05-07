# While Loop = Execute some code WHILE some condition remains True

# ---------------------------------------------------------
print()
Name = input("Enter Your Name : ")

while Name == "" :
    print("You Did Not Enter Your Name!")
    print()
    Name = input("Enter Your Name : ")

print(f"Hello {Name}")

# ---------------------------------------------------------
print()
Age = int(input("Enter Your Age : "))

while Age < 0 :
    print("Age Can't Be Negative!")
    print()
    Age = int(input("Enter Your Age : "))

print(f"You Are {Age} Years Old")

# ---------------------------------------------------------
print()
Food = input("Enter A Food You Like (Q To Quit) : ")

while not Food == "Q" :
    print(f"You Like {Food}")
    print()
    Food = input("Enter A Food You Like (Q To Quit) : ")

print("Bye!")

# ---------------------------------------------------------
print()
Num = int(input("Enter A # Between 1-10 : "))

while Num < 1 or Num > 10 :
    print(f"{Num} Is Not Valid!")
    print()
    Num = int(input("Enter A # Between 1-10 : "))

print(f"Your Number Is {Num}")