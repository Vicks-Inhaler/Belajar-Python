# ======================================================
# Python Weight Converter

Weight = float(input("Enter Your Weight : "))
Unit = input("Kilograms or Pounds? (K or L) : ")

print()
if Unit == "K" :
    Weight = Weight * 2.205
    Unit = "Lbs."
elif Unit == "L" :
    Weight = Weight / 2.205
    Unit = "Kgs."
else :
    print(f"{Unit} Was Not Valid!")

print(f"Your Weight Is : {Weight} {Unit}")
print(f"Your Weight Is : {round(Weight, 1)} {Unit}")

# ---------------------------------------------------
print()
if Unit == "K" :
    Weight = Weight * 2.205
    Unit = "Lbs."
    print(f"Your Weight Is : {round(Weight, 1)} {Unit}")
elif Unit == "L" :
    Weight = Weight / 2.205
    Unit = "Kgs."
else :
    print(f"{Unit} Was Not Valid!")

# ======================================================
# Python Suhu Converter
print()
Suhu = input("Is This Temperature In Celsius or Fahrenheit (C/F) : ")
Temp = float(input("Enter The Temperature : "))

print()
if Suhu == "C" :
    pass
elif Suhu == "F" :
    pass
else :
    print(f"{Suhu} Is An Invalid Suhu Of Measurement")

# ---------------------------------------------------
print()
if Suhu == "C" :
    Temp = round((9 * Temp) / 5 + 32, 1) # Rumus Fahrenheit, °F = (°C X 9 / 5) + 32
    print(f"The Temperature In Fahrenheit Is : {Temp} °F")
elif Suhu == "F" :
    Temp = round((Temp - 32) * 5 / 9, 1) # Rumus Celsius, °C = (°F - 32) X 5 / 9
    print(f"The Temperature In Celsius Is : {Temp} °C")
else :
    print(f"{Suhu} Is An Invalid Suhu Of Measurement")