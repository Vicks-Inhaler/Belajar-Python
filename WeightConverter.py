# Python Weight Converter

Weight = float(input("Enter Your Weight : "))
Unit = input("Kilograms or Pounds? (K or L) : ")

if Unit == "K" :
    Weight = Weight * 2.205
    Unit = "Lbs"
    print(f"Your Weight is : {round(Weight, 1)} {Unit}")

elif Unit == "L" :
    Weight = Weight / 2.205
    Unit = "Kgs"
    print(f"Your Weight is : {round(Weight, 1)} {Unit}")

else :
    print(f"{Unit} was Not Valid!")

# print(f"Your Weight is : {Weight} {Unit}")
# print(f"Your Weight is : {round(Weight, 1)} {Unit}")