# Return = Statement Used To End A Function
#          and Send A Result Back To The Caller

print()
def Add (X, Y) :
    Z = X + Y
    return Z

def Subtract (X, Y) :
    Z = X - Y
    return Z

def Multiply (X, Y) :
    Z = X * Y
    return Z

def Divide (X, Y) :
    Z = X / Y
    return Z

print(Add(1, 2))
print(Subtract(1, 2))
print(Multiply(1, 2))
print(Divide(1, 2))

print()
print("========================================")
def Create_Name (First, Last) :
    First = First.capitalize()
    Last = Last.capitalize()
    return First + " " + Last

Full_Name = Create_Name("Kadal", "Mesir")

print(Full_Name)