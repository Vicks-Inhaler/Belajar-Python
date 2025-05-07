# ==================================================================
# Exercise 1 Rectangle Area Calc

Length = float(input("Enter The Length : "))
Width = float(input("Enter The Width : "))
Area = Length * Width

print(Area)
print(f"The Area is : {Area} cm²")
print()
# ==================================================================
# Exercise 2 Shopping Chart Program

Item = input("What Item Would You Like To Buy? : ")
Price = float(input("What Is The Price? : $"))
Quantity = int(input("How Many Would You Like? : "))
Total = Price * Quantity

print(Total)
print()
print(f"You Have Bought {Quantity} x {Item}/s")
print(f"Your Total Is : ${Total}")

# Note ==>
# Windows = Numlock + Alt + 0178 or Jika tidak ada tombol numerik
# Windows = Windows + R, ketik charmap, lalu tekan Enter.
#           Cari ² atau langsung scroll hingga menemukan ².
#           Klik Select, lalu Copy.
#           Tempel (Ctrl + V) di PyCharm atau teks editor lain.