# Nested Loop = A loop within another loop (Outer, Inner)
#               Outer Loop :
#                   Inner Loop :

# ----------------------------------------------------------------------------------
print()
for Counter in range(1, 10) :
    print(Counter, end="") # Tanpa Spasi (X, end=""), & Dengan Spasi (X, end=" ")

# ----------------------------------------------------------------------------------
print()
# Perulangan sebanyak X => range(X)
for Repeat in range(3) :
    for Counter in range(1, 10) :
        print(Counter, end="")
    # print() # Jika Ingin Berjajar ke baris dibawahnya

# ----------------------------------------------------------------------------------
print()
print()
Rows = int(input("Enter The # Of Rows : "))
Column = int(input("Enter The # Of Columns : "))
Symbol = input("Enter A Symbol To Use : ")

print()
for Repeat in range(Rows) :
    for Counter in range(Column) :
        print(Symbol, end="")
    print()