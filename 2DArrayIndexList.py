# 2 Dimensi List Index Array

print()
Fruits0 =        ["Apple", "Orange", "Banana", "Coconut"]
Fruits =        ["Apple", "Orange", "Banana", "Coconut"]
Vegetables =    ["Celery", "Carrots", "Potatoes"]
Meats =         ["Chicken", "Fish", "Turkey"]

Fruits0[0] = "Jambu"
Groceries = [Fruits, Vegetables, Meats]
Groceries1 = [["Apple", "Orange", "Banana", "Coconut"],
              ["Celery", "Carrots", "Potatoes"],
              ["Chicken", "Fish", "Turkey"]]
Groceries2 = [["Apple", "Orange", "Banana", "Coconut"],
              ["Celery", "Carrots", "Potatoes"],
              ["Chicken", "Fish", "Turkey"]]
Groceries3 = (("Apple", "Orange", "Banana", "Coconut"),
              ("Celery", "Carrots", "Potatoes"),
              ("Chicken", "Fish", "Turkey"))
# Dengan {} Maka Setiap Running Program Data Didalam Index Array Akan Ditampilkan Acak Tetap Sesuai Data Dalam 1 Array Index
Groceries4 = ({"Apple", "Orange", "Banana", "Coconut"},
              {"Celery", "Carrots", "Potatoes"},
              {"Chicken", "Fish", "Turkey"})

print(Fruits0)
print(Groceries)
print(Groceries[1])             # Or print(Groceries[0]) Or print(Groceries[2])
print(Groceries[2][2])          # Or print(Groceries[1][1]) Or print(Groceries[2][1]) Or dst Max [2][2]

print()
for Collection in Groceries1 :
    print(Collection)

print()
for Collection1 in Groceries2 :
    for Food in Collection1 :
        # print(Food)           # Tanpa Ada Spasi Or
        print(Food, end=" ")    # Dengan Spasi Sejajar
    print()                     # Untuk Memisahkan Setiap Baris Hasil Index

print()
for Collection2 in Groceries3 :
    for Food1 in Collection2 :
        # print(Food)           # Tanpa Ada Spasi Or
        print(Food1, end=" ")    # Dengan Spasi Sejajar
    print()                     # Untuk Memisahkan Setiap Baris Hasil Index

print()
for Collection3 in Groceries4 :
    for Food2 in Collection3 :
        # print(Food)           # Tanpa Ada Spasi Or
        print(Food2, end=" ")    # Dengan Spasi Sejajar
    print()                     # Untuk Memisahkan Setiap Baris Hasil Index