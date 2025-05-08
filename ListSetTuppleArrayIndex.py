# Collection = Single "Variable" used to store multiple values
# List = [] Ordered and Changeable. Duplicates OK
# Set = {} UnOrdered and Immutable, but Add/Remove OK. No Duplicates
# Tupple = () Ordered and UnChangeable. Duplicates OK. FASTER

# =======================================================================
# Example List []
# ----------------------------------------------------------------------
print()
print("=================================================")
print("EXAMPLE LIST []")
print("=================================================")
Fruits = ["Apple", "Orange", "Banana", "Coconut"]
Fruits1 = ["Apple", "Orange", "Banana", "Coconut"]
Fruits2 = ["Apple", "Orange", "Banana", "Coconut"]
Fruits3 = ["Apple", "Orange", "Banana", "Coconut"]
Fruits4 = ["Apple", "Orange", "Banana", "Coconut"]
Fruits5 = ["Apple", "Orange", "Banana", "Coconut"]
Fruits6 = ["Apple", "Orange", "Banana", "Coconut"]
Fruits7 = ["Apple", "Orange", "Banana", "Coconut"]
Fruits8 = ["Apple", "Orange", "Banana", "Coconut"]
Fruits9 = ["Apple", "Orange", "Banana", "Coconut"]

Fruits1[0] = "PineApple"        # Replace to Data Index [0] => Fruits = ["Aple", "Orange", "Banana", "Coconut"]
Fruits1[1] = "Jambu"            # Replace to Data Index [1]
Fruits2.append("Anggur")        # Menambahkan Data Baris Terakhir Sesuai Data Yang DiPerintahkan
Fruits3.remove("Banana")        # Menghapus Data Index Sesuai Data Yang Dituju
Fruits4.insert(3, "Gedang")     # Menyisipkan Data Ke Index Yang Sudah Ada
Fruits5.sort()                  # Menampilkan Data Index Sesuai Abjad
Fruits6.reverse()               # Menampilkan Index Dari Data Paling Terakhir
Fruits7.sort()                  # Menampilkan Data Index Sesuai Abjad Kemudian Dibalik Urutan Indexnya
Fruits7.reverse()               # Menampilkan Data Index Sesuai Abjad Kemudian Dibalik Urutan Indexnya
Fruits8.clear()                 # Membersihkan Data Index

for Fruit in Fruits :
    print(Fruit)

print()
print(Fruits)
print(Fruits[1])
print(Fruits[0:3])
print(Fruits[:4])
print(Fruits[::2])
print(Fruits[::-1])
# print(dir(Fruits))
# print(help(Fruits))
print(len(Fruits))
print("Apple" in Fruits)
print("Jambu" in Fruits)
print()
print(Fruits1)
print(Fruits2)
print(Fruits3)
print(Fruits4)
print(Fruits5)
print(Fruits6)
print(Fruits7)
print(Fruits8)
print()
print(Fruits9.index("Apple"))               # Mencari Letak Index Data Yang Ada di Index
print(Fruits9.index("Coconut"))             # Mencari Letak Index Data Yang Ada di Index
print(Fruits9.count("Banana"))              # Menghitung Data Yang Sesuai di Index

# =======================================================================
# Example Set {}
# ----------------------------------------------------------------------
print()
print("=================================================")
print("EXAMPLE SET {}")
print("=================================================")
print()
Fruits = {"Apple", "Orange", "Banana", "Coconut"}
Fruits1 = {"Apple", "Orange", "Banana", "Coconut"}
Fruits2 = {"Apple", "Orange", "Banana", "Coconut"}
Fruits3 = {"Apple", "Orange", "Banana", "Coconut"}
Fruits4 = {"Apple", "Orange", "Banana", "Coconut"}
Fruits5 = {"Apple", "Orange", "Banana", "Coconut", "Coconut"}

Fruits1.add("PineApple")            # Menyisipkan Data Index Secara Acak
Fruits2.remove("Apple")             # Menghapus Data Index Yang Sesuai Data
Fruits3.pop()                       # Menghapus Data Index Secara Acak
Fruits4.clear()                     # Menghapus Semua Data Index

# print(dir(Fruits))
# print(help(Fruits))
# print(len(Fruits))
print("Apple" in Fruits)
print("Jambu" in Fruits)
print(Fruits)
print(Fruits1)
print(Fruits2)
print(Fruits3)
print(Fruits4)
print(Fruits5)

# =======================================================================
# Example Tupple ()
# ----------------------------------------------------------------------
print()
Fruits = ("Apple", "Orange", "Banana", "Coconut", "Coconut")
Fruits1 = ("Apple", "Orange", "Banana", "Coconut", "Coconut")
Fruits2 = ("Apple", "Orange", "Banana", "Coconut", "Coconut")
Fruits3 = ("Apple", "Orange", "Banana", "Coconut", "Coconut")

# print(dir(Fruits))
# print(help(Fruits))
print(len(Fruits))
print(Fruits)
print("Apple" in Fruits)
print("Jambu" in Fruits)
print()
print(Fruits1.index("Apple"))               # Mencari Letak Index Data Yang Ada di Index
print(Fruits1)
print(Fruits2.count("Coconut"))             # Menghitung Data Yang Sesuai di Index
print(Fruits2)
print()
for Fruit in Fruits :
    print(Fruit)
print()
