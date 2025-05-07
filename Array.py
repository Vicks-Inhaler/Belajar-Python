# List [] = Mutable, most flexible
# Tuple () = Immutable, faster
# Set {} = Mutable (Add/Remove), Unordered, No Duplicates, Best for Membership Testing

#===============================
# Example List [] :
# Names = ["Kadal", "Mesir", "Kodal", "Mangan", "Jembut"]

# print(Names[0])
# print(Names[1])
# print(Names[2])
# print(Names[3])
# print(Names[4])
# print(Names[5)

# for Name in Names :
   # print(Name, end=" ")

#===============================
# Example Tuple () :
# Names = ["Kadal", "Mesir", "Kodal", "Mangan", "Jembut"]

# Names[2] = "Gondrong"
# Names.append("Gondrong")
# Names.remove("Mangan")
# Names.pop(1)
# Names.clear()

# for Name in Names :
   # print(Name, end=" ")

#===============================
# Example Set {} :
Names = {"Kadal", "Mesir", "Kodal", "Mangan", "Jembut"}

# Names.add("Gondrong")
# Names.remove("Jembut")
# Names.append("Gondrong")
# Names.pop()
# Names.clear()

#for Name in Names :
   # print(Name, end=" ")

# Example Logic
#--------------------------------
# if "Jembut" in Names :
    # print("Jembut Was Found")
# else :
    # print("Jembut Was Not Found")

# or
# if "Kunam" in Names :
    # print("Kunam Was Found")
# else :
    # print("Kunam Was Not Found")

# or
Name = input("Enter a Name to Search For : ")

if Name in Names :
    print(f"{Name} Was Found")
else :
    print(f"{Name} Was Not Found")
#--------------------------------