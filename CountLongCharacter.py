# =======================================================
print()
Name = input("Enter Your Full Name : ")

# Example Name = kadal mesir
Result = len(Name)
Result1 = Name.find(" ")
Result2 = Name.find("l")
Result3 = Name.rfind("r")
Result4 = Name.rfind("q")
Name1 = Name.capitalize()
Name2 = Name.upper()
Name3 = Name.lower()
Result5 = Name.isdigit()
Result6 = Name.isalpha()

print()
print(Result)
print(Result1)
print(Result2)
print(Result3)
print(Result4) # Hasil -1 artinya tidak ditemukan
print(Name1)
print(Name2)
print(Name3)
print(Result5) # False artinya tidak ada digit number (True jika Name = 12345)
print(Result6) # False artinya ada spasi antar kata (True jika Name = kadalmesir)

# =======================================================
print()
Phone_Number = input("Enter Your Phone : ")

# Example Phone_Number = 1-234-567-890
Review = Phone_Number.count("-")
Review1 = Phone_Number.replace("-", " ")
Review2 = Phone_Number.replace("-", "")

print()
print(Review)
print(Review1)
print(Review2)