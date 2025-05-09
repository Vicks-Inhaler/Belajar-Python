# Concession Stand Program
# Dictionary {Key:Value}

print()
Menu = {"Pizza": 3.00,
        "Nachos": 4.50,
        "PopCorn": 6.00,
        "Fries": 2.50,
        "Chips": 1.00,
        "Pretzel": 3.50,
        "Soda": 3.00,
        "Lemonade": 4.25}
Menu1 = {"Pizza": 3.00,
        "Nachos": 4.50,
        "PopCorn": 6.00,
        "Fries": 2.50,
        "Chips": 1.00,
        "Pretzel": 3.50,
        "Soda": 3.00,
        "Lemonade": 4.25}
Cart = []
Cart1 = []
Total = 0
Total1 = 0

print("VERSI 1")
print("------- MENU -------")
for Key, Value in Menu.items() :
    # print(f"{Key}: {Value}")                # Or
    # print(f"{Key}: ${Value:.2f}")           # Value dengan Mata Uang dan 2 angka desimal, Or
    print(f"{Key:10}: ${Value:.2f}")          # Dengan Key Sama Rata (:), Value dengan Mata Uang dan 2 angka desimal
print("--------------------")

while True :
    # Jika memakai huruf kecil baik itu "Menu = {"pizza"}" & "q" maka Food = input("Select An Item (Q To Quit) : ").lower()
    Food = input("Select An Item (Q To Quit) : ")
    if Food.upper() == "Q" :                            # Pakai if Food.lower() == "q" : => Jika quit dengan huruf kecil
        break
    elif Menu.get(Food) is not None :
        Cart.append(Food)
print()
print(Cart)

print()
print("======== YOUR ORDER ========")
for Food in Cart :
    Total += Menu.get(Food)
    print(Food, end=" ")
print()
print(f"Total Is : ${Total : .2f}")
print("============================")

# ==================================================================================================
print()
print("VERSI 2")
print("------- MENU -------")
for Key1, Value1 in Menu1.items() :
    # print(f"{Key}: {Value}")                # Or
    # print(f"{Key}: ${Value:.2f}")           # Value dengan Mata Uang dan 2 angka desimal, Or
    print(f"{Key1:10}: ${Value1:.2f}")          # Dengan Key Sama Rata (:), Value dengan Mata Uang dan 2 angka desimal
print("--------------------")

while True :
    # Jika memakai huruf kecil baik itu "Menu = {"pizza"}" & "q" maka Food = input("Select An Item (Q To Quit) : ").lower()
    Food1 = input("Select An Item (Q To Quit) : ")
    if Food1.upper() == "Q" :                            # Pakai if Food.lower() == "q" : => Jika quit dengan huruf kecil
        break
    elif Menu1.get(Food1) is not None :
        Cart1.append(Food1)
print()
print(Cart1)

print()
print("======== YOUR ORDER ========")
for Food1 in Cart1 :
    Total1 += Menu1.get(Food1)
    # print(Food, end=" ")
    print(f"{Food1:10}:             ${Menu1.get(Food1)}")
print("----------------------------")
print(f"Total Is :            ${Total1 : .2f}")
print("============================")