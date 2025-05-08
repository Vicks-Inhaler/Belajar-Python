# Dictionary = A Colection of {Key:Value} pairs
#              Ordered and Changeable. No Duplicates

print()
Capitals = {"USA" : "Washington D.C.",
            "India" : "New Delhi",
            "China" : "Beijing",
            "Indonesia" : "Jakarta"}
Capitals1 = {"USA" : "Washington D.C.",
            "India" : "New Delhi",
            "China" : "Beijing",
            "Indonesia" : "Jakarta"}
Capitals2 = {"USA" : "Washington D.C.",
            "India" : "New Delhi",
            "China" : "Beijing",
            "Indonesia" : "Jakarta"}
Capitals3 = {"USA" : "Washington D.C.",
            "India" : "New Delhi",
            "China" : "Beijing",
            "Indonesia" : "Jakarta"}
Capitals4 = {"USA" : "Washington D.C.",
            "India" : "New Delhi",
            "China" : "Beijing",
            "Indonesia" : "Jakarta"}

# print(dir(Capitals))
# print(help(Capitals))
print(Capitals.get("Indonesia"))
print(Capitals.get("Rusia"))
print()
if Capitals.get("Indonesia") :
    print("That Capital Exist")
else :
    print("That Capital Doesn't Exist")
if Capitals.get("Rusia") :
    print("That Capital Exist")
else :
    print("That Capital Doesn't Exist")

print()
Capitals1.update({"Germany" : "Berlin"})
Capitals1.update({"USA" : "Detroit"})
print(Capitals1)

print()
Capitals2.pop("China")
print(Capitals2)

print()
Capitals3.popitem()                             # Menghapus Array Index Terakhir
print(Capitals3)

print()
Capitals4.clear()                               # Menghapus Semua Isi Array Index
print(Capitals4)

# Keys = Array Index Key dari {Key:Value}
# ======================================================================================
print()
Keys = Capitals.keys()
print(Keys)

for Key in Capitals.keys() :
    print(Key)

# Values = Array Index Value dari {Key:Value}
# ======================================================================================
print()
Values = Capitals.values()
print(Values)

for Value in Capitals.values() :
    print(Value)

# Items = Array Index Item Keduanya (Key : Value) dari {Key:Value}
# ======================================================================================
print()
Items = Capitals.items()
print(Items)

for Key, Value in Capitals.items() :
    print(f"{Key} : {Value}")