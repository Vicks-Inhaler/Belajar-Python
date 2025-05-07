# Conditional Expression = A one-line shorcut for the if-else statement (Ternary Operator)
#                          Print or assign one of two values based on a condition
#                          X if condition else Y

print()
# A one-line shorcut for the if-else statement (Ternary Operator)
Num = 5
Num1 = -5

# Print or assign one of two values based on a condition
Num2 = 6
Num3 = 7

# X if condition else Y
Num4 = 5
A = 6
B = 7
Age = 25
Age1 = 15
Temperature = 30
Temperature1 = 18
User_Role = "Admin"
User_Role1 = "Guest"

# A one-line shorcut for the if-else statement (Ternary Operator)
print("Positive" if Num > 0 else "Negative")
print("Positive" if Num1 > 0 else "Negative")

# Print or assign one of two values based on a condition
Result = "EVEN" if Num2 % 2 == 0 else "ODD"
Result1 = "EVEN" if Num3 % 2 == 0 else "ODD"
print()
print(Result)
print(Result1)

# X if condition else Y
Max_Num = A if A > B else B
Min_Num = A if A < B else B
Status = "Adult" if Age >= 18 else "Child"
Status1 = "Adult" if Age1 >= 18 else "Child"
Weather = "HOT" if Temperature > 20 else "COLD"
Weather1 = "HOT" if Temperature1 > 20 else "COLD"
Access_Level = "Full Access" if User_Role == "Admin" else "Limited Access"
Access_Level1 = "Full Access" if User_Role1 == "Admin" else "Limited Access"

print()
print(Max_Num)
print(Min_Num)
print(Status)
print(Status1)
print(Weather)
print(Weather1)
print(Access_Level)
print(Access_Level1)