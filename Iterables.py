# Iterables = An Object/Collection That Can Return Its Elements One At A Time,
#             Allowing It To Be  Iterated Over In A Loop

print()
Numbers = [1, 2, 3, 4, 5]
Numbers1 = (1, 2, 3, 4, 5)

for Number in Numbers :
    print(Number)
# # Or
# for Item in Numbers :
#     print(Item)

print()
for Number1 in Numbers1 :
    print(Number1)

print()
print("----- DIBALIK -----")
for Number in reversed(Numbers) :
    print(Number)
for Number in reversed(Numbers) :
    print(Number, end=" ")

print()
for Nilai in reversed(Numbers):
    print(Nilai, end="-")

print()
for Angka in reversed(Numbers):
    print(Angka, end=" - ")

print()
print("====== EXAMPLE ======")
Fruits = {"Apple", "Orange", "Banana", "Coconut"}

for Fruit in Fruits :
    print(Fruit)

print()
Name = "Kadal"

for Character in Name :
    print(Character, end=" ")

My_Dictionary = {"A" : 1, "B" : 2, "C" : 3}
print()
print()
for Key in My_Dictionary :
    print(Key)
print()
for Value in My_Dictionary.values() :
    print(Value)
print()
for Keys, Values in My_Dictionary.items() :
    print(Keys, Values)
    print(f"{Keys} = {Values}")