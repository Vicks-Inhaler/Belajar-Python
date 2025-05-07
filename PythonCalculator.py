# Python Calculator

Operator = input("Enter An Operator (+ - * /) : ")

Num1 = input("Enter The 1st Number : ")
Num2 = input("Enter The 2nd Number : ")

print(Num1 + Num2)

print()
Num3 = float(input("Enter The 3rd Number : "))
Num4 = float(input("Enter The 4th Number : "))
print(Num3 + Num4)

# ==================================================
print()
Simbol = input("Enter An Operator (+ - * /) : ")

Num5 = float(input("Enter The 5th Number : "))
Num6 = float(input("Enter The 6th Number : "))

if Simbol == "+" :
    Result = Num5 + Num6
    print(Result)
elif Simbol == "-" :
    Result = Num5 - Num6
    print(Result)
elif Simbol == "*" :
    Result = Num5 * Num6
    print(Result)
elif Simbol == "/" :
    Result = Num5 / Num6
    print(Result)
else :
    print(f"{Simbol} Is Not Valid!")

# -------------------------------------------------
if Simbol == "+" :
    Result = Num5 + Num6
    print(round(Result))
elif Simbol == "-" :
    Result = Num5 - Num6
    print(round(Result))
elif Simbol == "*" :
    Result = Num5 * Num6
    print(round(Result))
elif Simbol == "/" :
    Result = Num5 / Num6
    print(round(Result))
else :
    print(f"{Simbol} Is Not Valid!")

# -------------------------------------------------
if Simbol == "+" :
    Result = Num5 + Num6
    print(round(Result, 3))
elif Simbol == "-" :
    Result = Num5 - Num6
    print(round(Result, 3))
elif Simbol == "*" :
    Result = Num5 * Num6
    print(round(Result, 3))
elif Simbol == "/" :
    Result = Num5 / Num6
    print(round(Result, 3))
else :
    print(f"{Simbol} Is Not Valid!")