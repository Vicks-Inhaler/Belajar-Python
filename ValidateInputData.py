# Validate user input exercise
# 1. Username is no more than 12 characters
# 2. Username must not contain spaces
# 3. Username must not contain digits

print()
Username = input("Enter A Username : ")

# 1. Username is no more than 12 characters
# ------------------------------------------------------------
print()
# Example Username = Kadal Mesir1
if len(Username) > 12 :
    print("Your Username Can't Be More Than 12 Characters") # Username Maximal 12 Huruf
else :
    print(f"Welcome {Username}")  # Cetak Jika Logic Sesuai

# 2. Username must not contain spaces
# ------------------------------------------------------------
if len(Username) > 12 :
    print("Your Username Can't Be More Than 12 Characters") # Username Maximal 12 Huruf
elif not Username.find(" ") == -1 :
    print("Your Username Can't Contain Spaces") # Username Harus Tanpa Spasi mis. KadalMesir1
else :
    print(f"Welcome {Username}") # Cetak Jika Logic Sesuai

# 3. Username must not contain digits
if len(Username) > 12 :
    print("Your Username Can't Be More Than 12 Characters") # Username Maximal 12 Huruf
elif not Username.find(" ") == -1 :
    print("Your Username Can't Contain Spaces") # Username = KadalMesir1
elif not Username.isalpha() :
    print("Your Username Can't Contain Numbers") # Username Tidak Boleh Ada Digit Number mis. KadalMesir123
else :
    print(f"Welcome {Username}") # Cetak Jika Logic Sesuai