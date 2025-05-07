name = input("Enter Your Name : ")

while name == "":
    name = input("Enter Your Name : ")

age = int(input("Enter Your Age : "))

while age < 17 :
    print("Age Can't be Less Than 17")
    age = int(input("Enter Your Age : "))

print(f"Hello {name}!")
print(f"You are {age} Years Old!")