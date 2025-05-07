# Python Compound Interest Calculator
Priciple = 0
Rate = 0
Time = 0

while Priciple <= 0 :
    print()
    Priciple = float(input("Enter The Principle Amount : "))
    if Priciple <= 0 :
        print("Principle Can't Be Less Than Or Equal To Zero")

while Rate <= 0 :
    Rate = float(input("Enter The Interest Rate : "))
    if Rate <= 0 :
        print("Interest Rate Can't Be Less Than Or Equal To Zero")

while Time <= 0 :
    Time = int(input("Enter The Time In Years : "))
    if Time <= 0 :
        print("Time Can't Be Less Than Or Equal To Zero")

Total = Priciple * pow((1 + Rate / 100), Time)

print()
print(Priciple)
print(Rate)
print(Time)
print()
print(f"Balance After {Time} Year/s : ${Total:.2f}")

# ---------------------------------------------------------------------
while True :
    print()
    Priciple = float(input("Enter The Principle Amount : "))
    if Priciple < 0:
        print("Principle Can't Be Less Than Zero")
    else:
        break

while True :
    Rate = float(input("Enter The Interest Rate : "))
    if Rate < 0:
        print("Interest Rate Can't Be Less Than Zero")
    else :
        break

while True :
    Time = int(input("Enter The Time In Years : "))
    if Time < 0 :
        print("Time Can't Be Less Than Zero")
    else :
        break

Total = Priciple * pow((1 + Rate / 100), Time)

print()
print(f"Balance After {Time} Year/s : ${Total:.2f}")