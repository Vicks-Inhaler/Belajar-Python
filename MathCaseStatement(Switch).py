# Math-Case Statement (Switch) = An alternative to using many 'elif' statements
#                                Execute some code if a value matches a 'case'
#                                Benefits : Cleaner and Syntaxs is more readable

print()
print("====== If Else ======")
def Day_Of_Week (Day) :
    if Day == 1 :
        return "It is Sunday"
    elif Day == 2 :
        return "It is Monday"
    elif Day == 3 :
        return "It is Tuesday"
    elif Day == 4 :
        return "It is Wednesday"
    elif Day == 5 :
        return "It is Thursday"
    elif Day == 6 :
        return "It is Friday"
    elif Day == 7 :
        return "It is Saturday"
    else :
        return "Not a Valid Day"

print(Day_Of_Week(1))
print(Day_Of_Week("Kadal"))

print()
print("====== Case Numbers ======")
def Day_Of_Week (Day) :
    match Day :                                 # Hanya berjalan di Python Versi 3.10 keatas
        case 1 :
            return  "It is Sunday"
        case 2 :
            return "It is Monday"
        case 3 :
            return "It is Tuesday"
        case 4 :
            return "It is Wednesday"
        case 5 :
            return "It is Thursday"
        case 6 :
            return "It is Friday"
        case 7 :
            return "It is Saturday"
        case _ :
            return "Not a Valid Day"

print(Day_Of_Week(1))
print(Day_Of_Week("Kadal"))

print()
print("====== Case String ======")
def Is_Weekend (Day) :
    match Day :                                 # Hanya berjalan di Python Versi 3.10 keatas
        case "Sunday" :
            return  True
        case "Monday" :
            return False
        case "Tuesday" :
            return False
        case "Wednesday" :
            return False
        case "Thursday" :
            return False
        case "Friday" :
            return False
        case "Saturday" :
            return True
        case _ :
            return False

print(Day_Of_Week("Monday"))
print(Day_Of_Week("Kadal"))

print(Day_Of_Week(1))
print(Day_Of_Week("Kadal"))

print()
print("====== Short Case ======")
def Is_Weekend (Day) :
    match Day :                                 # Hanya berjalan di Python Versi 3.10 keatas
        case "Saturday" | "Sunday" :
            return  True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday" :
            return False
        case _ :
            return False

print(Day_Of_Week("Sunday"))
print(Day_Of_Week("Monday"))
print(Day_Of_Week("Kadal"))