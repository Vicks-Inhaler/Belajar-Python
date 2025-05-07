# Logical Operator = Evaluate multiple conditions (Or, And, Not)
#                    Or = At least one condition must be True
#                    And = Both conditions must be True
#                    Not = Inverts the condition (not False, not True)

# =========================================================
# Or
print()
Temp = 25
Is_Raining = False

if Temp > 35 or Temp < 0 or Is_Raining :
    print("The Outdoor Event Is Canceled")
else :
    print("The Outdoor Event Is Still Scheduled")
# --------------------------------------------------------
Temp = 36
Is_Raining = False

if Temp > 35 or Temp < 0 or Is_Raining :
    print("The Outdoor Event Is Canceled")
else :
    print("The Outdoor Event Is Still Scheduled")
# --------------------------------------------------------
Temp = -5
Is_Raining = False

if Temp > 35 or Temp < 0 or Is_Raining :
    print("The Outdoor Event Is Canceled")
else :
    print("The Outdoor Event Is Still Scheduled")
# --------------------------------------------------------
Temp = 20
Is_Raining = True

if Temp > 35 or Temp < 0 or Is_Raining :
    print("The Outdoor Event Is Canceled")
else :
    print("The Outdoor Event Is Still Scheduled")

# =========================================================
# And

print()
Temp = 20
Is_Sunny = True

if Temp >= 28 and Is_Sunny :
    print("It is HOT Outside ♨")
    print("It is SUNNY 🌸")
elif Temp <= 0 and Is_Sunny :
    print("It is COLD Outside ❄")
    print("It is SUNNY 🌸")
elif 28 > Temp > 0 and Is_Sunny :
    print("It is WARM Outside 😪")
    print("It is SUNNY 🌸")

# =========================================================
# Not

print()
Temp = 28
Is_Sunny = False

if Temp >= 28 and not Is_Sunny :
    print("It is HOT Outside ♨")
    print("It is CLOUDY 🌸")
elif Temp <= 0 and not Is_Sunny :
    print("It is COLD Outside ❄")
    print("It is CLOUDY 🌸")
elif 28 > Temp > 0 and not Is_Sunny :
    print("It is WARM Outside 😪")
    print("It is CLOUDY 🌸")
