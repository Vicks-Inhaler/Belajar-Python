# Shopping Cart Program

print()
Foods = []
Prices = []
Total = 0
Foods1 = []
Prices1 = []
Total1 = 0
Foods2 = []
Prices2 = []
Total2 = 0

while True :
    Food = input("Enter A Food To Buy (Q To Quit) : ")
    if Food.upper() == "Q" :            # if Food.lower() == "Q" : Jika menggunakan huruf "q" kecil
        break

# -------------------------------------------------------------------------------------------------
print()
while True :
    Food1 = input("Enter A Food To Buy (Q To Quit) : ")
    if Food1.upper() == "Q":  # if Food.lower() == "Q" : Jika menggunakan huruf "q" kecil
            break
    else :
        Price1 = float(input(f"Enter The Price Of A {Food1} : $"))
        Foods1.append(Food1)
        Prices1.append(Price1)

# -------------------------------------------------------------------------------------------------
print()
while True :
    Food2 = input("Enter A Food To Buy (Q To Quit) : ")
    if Food2.upper() == "Q":  # if Food.lower() == "Q" : Jika menggunakan huruf "q" kecil
            break
    else :
        Price2 = float(input(f"Enter The Price Of A {Food2} : $"))
        Foods2.append(Food2)
        Prices2.append(Price2)

print("----- YOUR CART -----")

for Food2 in Foods2 :
    # print(Food2)                  # Cetak PerBaris Atau
    print(Food2, end=" ")           # Cetak Satu Baris Dengan Spasi

for Price2 in Prices2 :
    Total2 += Price2

print()
print(f"Your Total Is : ${Total2}")