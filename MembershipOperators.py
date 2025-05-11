# Membership Opertors = Used to test whether a value or variable is found in a sequence
#                       (String, List, Tuple, Set, or Dictionary)
#                       1. in
#                       2. not in

# # String, List, Tuple, Set
# print()
# print("========== String, List, Tuple, Set ==========")
# Word = "APPLE"
# Letter = input("Guess a Letter in the Secret World (A, B, C, or etc): ")
#
# if Letter in Word :
#     print(f"There is a {Letter}")
# else :
#     print(f"{Letter} was Not Found!")
#
# if Letter not in Word :
#     print(f"{Letter} was Not Found!")
# else :
#     print(f"There is a {Letter}")
#
# # ============================================
# print()
# Students = {"Kadal", "Mesir", "Kodal"}
# Student = input("Enter the Name of a Student : ")
#
# if Student in Students :
#     print(f"{Student} is a Student")
# else :
#     print(f"{Student} was Not Found!")
#
# if Student not in Students :
#     print(f"{Student} was Not Found!")
# else :
#     print(f"{Student} is a Student")
#
# # Dictionary
# print()
# print("====== Dictionary =======")
# Grades = {"Kadal" : "A",
#           "Mesir" : "B",
#           "Kodal" : "C",
#           "Kunam" : "D"}
#
# Student = input("Enter the Name of a Student : ")
#
# if Student in Grades :
#     print(f"{Student}'s Grade is {Grades[Student]}")
# else :
#     print(f"{Student} was Not Found!")

print()
Email = "KadalMesirKodal@gmail.com"
Email1 = "KadalMesirKodalgmail.com"
Email2 = "KadalMesirKodal@gmailcom"

if "@" in Email and "." in Email :
    print("Valid Email")
else :
    print("Invalid Email!")

if "@" not in Email and "." not in Email :
    print("Invalid Email!")
else :
    print("Valid Email")

if "@" in Email1 and "." in Email1 :
    print("Valid Email")
else :
    print("Invalid Email!")

if "@" in Email2 and "." in Email2 :
    print("Valid Email")
else :
    print("Invalid Email!")

if "@" not in Email and "." not in Email :
    print("Invalid Email!")
else :
    print("Valid Email")

if "@" not in Email1 and "." not in Email1 :
    print("Valid Email")
else :
    print("Invalid Email!")