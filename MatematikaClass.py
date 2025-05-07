import math

# ==================================================================================================
X = 9
X1 = 9.1
X2 = 9.3

Result = math.sqrt(X) # Akar kuadrat dari X
Result1 = math.ceil(X1) # Pembulatan Nilai di belakang koma lebih dari 0.0, Menjadi Bilangan Bulat diatas nilai X
Result2 = math.floor(X2) # Pembulatan Nilai di belakang koma lebih dari 0.0, Menjadi Bilangan Bulat dibawah nilai X

print(math.pi)
print(math.e) # Menghitung konstanta Euler's number (e), logaritma natural ln(x)
print(math.exp(3)) # Menghitung e^3
print(Result)
print(Result1)
print(Result2)

# ==================================================================================================
Radius = float(input('Enter The Radius Of A Circle : '))

Circumference = 2 * math.pi * Radius # C = 2 ᴨ r
Area = math.pi * pow(Radius, 2) # A = ᴨ r²

print(f"The Circumference Is : {Circumference} cm")
print(f"The Circumference Is : {round(Circumference, 2)} cm") # Pemendekan angka dibelakang koma menjadi 0.00
print(f"The Area Of Circle Is : {Area} cm²")
print(f"The Area Of Circle Is : {round(Area, 2)} cm²")

# ==================================================================================================
A = float(input("Enter Side A : "))
B = float(input("Enter Side B : "))

C = math.sqrt(pow(A, 2) + pow(B, 2)) # C = √ A² + B² Rumus Phytagoras (Sisi Segitiga)

print(f"Side C = {C}")