# List Comprehension = A Concise way to create  lists in Python
#                      Compact and easier to read than traditional Loops
#                      [Expression for value in iterable if condition]

print()
# Note => Doubles = [Expression for value in iterable if condition]
Doubles = []
Doubles1 = [X * 2 for X in range(1, 11)]            # Kelipatan 2 dari Nilai 1-10
Triples = [X * 3 for X in range(1, 11)]             # Kelipatan 3 dari Nilai 1-10
Squares = [Z * Z for Z in range(1, 11)]             # Kuadrat dari Nilai 1-10

for X in range(1, 11) :
    Doubles.append(X * 2)

print(Doubles)
print(Doubles1)
print(Triples)
print(Squares)

print()
print("====== EXAMPLE ======")
Fruits = ["apple", "orange", "banana", "coconut"]
Fruits1 = ["APPLE", "ORANGE", "BANANA", "COCONUT"]
Fruits2 = ["apple", "orange", "banana", "coconut"]

Fruits = [Fruit.upper() for Fruit in Fruits]
Fruits1 = [Fruit1.lower() for Fruit1 in Fruits1]
Fruit_Chars2 = [Fruit2[0] for Fruit2 in Fruits2]

print(Fruits)
print(Fruits1)
print(Fruit_Chars2)

print()
print("------ Numbers ------")
Numbers = [1, -2, 3, -4, 5, -6, 8, -7]

Positive_Nums = [Num for Num in Numbers if Num >= 0]
Negative_Nums = [Num for Num in Numbers if Num < 0]
Even_Nums = [Num for Num in Numbers if Num % 2 == 0]
Odd_Nums = [Num for Num in Numbers if Num % 2 == 1]

print(Positive_Nums)
print(Negative_Nums)
print(Even_Nums)
print(Odd_Nums)

print()
print("------ Grades ------")
Grades = [85, 42, 79, 90, 56, 61, 30]

Passing_Grades = [Grade for Grade in Grades if Grade >= 60]

print(Passing_Grades)