# Default Arguments = A Default Value For Certain  Parameters
#                     default is used when that argument is omitted
#                     make your functions more flexible, reduces # of arguments
#                     1. Positional, 2. DEFAULT, 3. Keyword, 4. ARBITRARY
# Note For ARBITRARY :
# *Args             = Allows You To Pass Multiple Non-Key Arguments
# **KwArgs          = Allows You To Pass Multiple Keyword-Arguments
#                     * Unpacking Operator
#                     1. Positional, 2. DEFAULT, 3. Keyword, 4. ARBITRARY

print()
print("=========== DEFAULT ===========")
print("========== NET PRICE ==========")
def Net_Price (List_Price, Discount, Tax) :
    return List_Price * (1 - Discount) * (1 + Tax)

def Net_Price1 (List_Price1, Discount1 = 0, Tax1 = 0.05) :
    return List_Price1 * (1 - Discount1) * (1 + Tax1)

def Net_Price2 (List_Price2, Discount2 = 0, Tax2 = 0.05) :
    return List_Price2 * (1 - Discount2) * (1 + Tax2)

def Net_Price3 (List_Price3, Discount3 = 0, Tax3 = 0.05) :
    return List_Price3 * (1 - Discount3) * (1 + Tax3)

print(Net_Price(500, 0, 0.05))
print(Net_Price1(500))
print(Net_Price2(500, 0.1))
print(Net_Price3(500, 0.1, 0))

print()
print("========== COUNT ==========")
import time

def Count (Start, End) :
    print("------ EXAMPLE COUNT 1 ------")
    for X in range (Start, End + 1) :
        print(X)
        time.sleep(1)
    print("DONE!")
    print()

def Count1 (End1, Start1 = 0) :
    print("------ EXAMPLE COUNT 2 ------")
    for X1 in range (Start1, End1 + 1) :
        print(X1)
        time.sleep(1)
    print("DONE!")
    print()

def Count2 (End2, Start2 = 0) :
    print("------ EXAMPLE COUNT 3 ------")
    for X2 in range (Start2, End2 + 1) :
        print(X2)
        time.sleep(1)
    print("DONE!")
    print()

Count(0, 10)
Count1(10)
Count2(30, 15)

print()
print("============= KEYWORD ==============")
def Hello (Greeting, Title, First, Last) :
    print(f"{Greeting} {Title} {First} {Last}")

def Hello1 (Greeting1, Title1, First1, Last1) :
    print(f"{Greeting1} {Title1} {First1} {Last1}")

Hello("Hello", "Mr.", "Kadal", "Mesir")
Hello("Hello", Title="Mr.", First="Kadal", Last="Mesir")
Hello1("Hello1", Title1="Mr.", Last1="Kadal", First1="Mesir")

print()
print("---------- EXAMPLE KEYWORD ----------")
for X in range (1, 10) :
    print(X, end=" ")
print()
print("1", "2", "3", "4", "5", sep="-")

print()
def Get_Phone (Country, Area, First, Last) :
    return f"{Country}-{Area}-{First}-{Last}"
Phone_Num = Get_Phone(Country=1, Area=123, First=456, Last=7890)
Phone_Num1 = Get_Phone(1, 123, 456, 7890)
print(Phone_Num)
print(Phone_Num1)

print()
print("============= ARBITRARY ==============")
# ---------- *Args -----------
print("---------- *Args ----------")
def Add (*Args) :
    Total = 0
    for Arg in Args :
        Total += Arg
    return Total

def Tambah (*Nums) :
    Jumlah = 0
    for Num in Nums :
        Jumlah += Num
    return Jumlah

print(Add(1, 2, 3, 4, 5))
print(Add(1))
print(Tambah(1, 2, 3, 4))
print(Tambah(3))

print()
print("---------- EXAMPLE *Args ----------")
def Display_Name (*Names) :
    # pass
    for Name in Names :
        print(Name, end=" ")
Display_Name("Dr.", "Kadal", "Mesir", "Kodal", "II")

# ---------- **KwArgs -----------
print()
print("---------- **KwArgs ----------")
def Print_Address (**KwArgs) :
    for Value in KwArgs.values() :
        print(Value)

def Print_Address1 (**KeyWord1) :
    for Key1 in KeyWord1.values() :
        print(Key1)

def Print_Address2 (**KeyWord2) :
    for Key2, Value2 in KeyWord2.items() :
        print(f"{Key2:10} : {Value2}")

Print_Address (Street = "123 Fake St.",
               City = "Detroit",
               State = "MI",
               ZIP = "54321")

print()
Print_Address1 (Street1 = "JL. Kadal Mesir",
                City1 = "Tulungagung",
                State1 = "JATIM",
                ZIP1 = "811986")

print()
Print_Address2 (Street2 = "JL. Candi Mendut",
                APT2 = "500",
                City2 = "Malang",
                State2 = "JATIM",
                ZIP2 = "881987")

print()
print("---------- EXAMPLE *KwArgs ----------")
def Shipping_Label (*Keys, **Keyword) :
    # pass
    for Key in Keys :
        print(Key, end=" ")
    print()

    for Value in Keyword.values() :
        print(Value, end=" ")
    print()

def Shipping_Label1 (*Keys1, **Keyword1) :
    # pass
    print()
    for Key1 in Keys1 :
        print(Key1, end=" ")
    print()
    print(f"{Keyword1.get('Street1')}")

def Shipping_Label2 (*Keys2, **Keyword2) :
    # pass
    print()
    for Key2 in Keys2:
        print(Key2, end=" ")
    print()
    print(f"{Keyword2.get('Street2')}")
    print(f"{Keyword2.get('City2')} {Keyword2.get('State2')}, {Keyword2.get('ZIP2')}")

def Shipping_Label3 (*Keys3, **Keyword3) :
    # pass
    print()
    for Key3 in Keys3:
        print(Key3, end=" ")
    print()
    print(f"{Keyword3.get('Street3')}, {Keyword3.get('APT3')}")
    print(f"{Keyword3.get('City3')} {Keyword3.get('State3')}, {Keyword3.get('ZIP3')}")

def Shipping_Label4 (*Keys4, **Keyword4) :
    # pass
    print()
    for Key4 in Keys4:
        print(Key4, end=" ")
    print()
    print(f"{Keyword4.get('Street4')}, {Keyword4.get('APT4')}")
    print(f"{Keyword4.get('City4')} {Keyword4.get('State4')}, {Keyword4.get('ZIP4')}")

def Shipping_Label5 (*Keys5, **Keyword5) :
    # pass
    print()
    for Key5 in Keys5:
        print(Key5, end=" ")
    print()
    if "APT5" in Keyword5 :
        print(f"{Keyword5.get('Street5')} {Keyword5.get('APT5')}")
    elif "PO_BOX5" in Keyword5 :
        print(f"{Keyword5.get('Street5')}")
        print(f"{Keyword5.get('PO_BOX5')}")
    else :
        print(f"{Keyword5.get('Street5')}")

    print(f"{Keyword5.get('City5')} {Keyword5.get('State5')}, {Keyword5.get('ZIP5')}")

Shipping_Label("Dr.", "Kadal", "Mesir", "Kodal",
               Street = "JL. Karangwaru 69",
               APT = "200",
               PO_BOX = "#5123",
               City = "Tulungagung",
               State = "JATIM",
               ZIP = "05012020")

Shipping_Label1("Dr.", "Kadal", "Mesir", "Kodal",
               Street1 = "JL. Karangwaru 69",
               APT1 = "#150",
               PO_BOX1 = "#5123",
               City1 = "Tulungagung",
               State1 = "JATIM",
               ZIP1 = "05012020")

Shipping_Label2("Dr.", "Kadal", "Mesir", "Kodal",
               Street2 = "JL. Karangwaru 69",
               APT2 = "#150",
               PO_BOX2 = "#5123",
               City2 = "Tulungagung",
               State2 = "JATIM",
               ZIP2 = "05012020")

Shipping_Label3("Dr.", "Kadal", "Mesir", "Kodal",
               Street3 = "JL. Karangwaru 69",
               APT3 = "#150",
               PO_BOX3 = "#5123",
               City3 = "Tulungagung",
               State3 = "JATIM",
               ZIP3 = "05012020")

Shipping_Label4("Dr.", "Kadal", "Mesir", "Kodal",
               Street4 = "JL. Karangwaru 69",
               # APT41 = "#150",
               PO_BOX4 = "#5123",
               City4 = "Tulungagung",
               State4 = "JATIM",
               ZIP4 = "05012020")

Shipping_Label5("Dr.", "Kadal", "Mesir", "Kodal",
               Street5 = "JL. Karangwaru 69",
               # APT5 = "200",                                        # | Pake APT Atau diabwah ini
               PO_BOX5 = "PO BOX #5123",                              # | Memakai PO BOX Pilih salah satu
               City5 = "Tulungagung",
               State5 = "JATIM",
               ZIP5 = "05012020")