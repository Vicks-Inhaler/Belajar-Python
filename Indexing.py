# Indexing = Accessing elements of a sequence using [] (Indexing Operator)
#            [Start : End : Step]

print()
Credit_Number = "1234-5678-9012-3456"

Last_Digits = Credit_Number[-4:] # Index 4 Digits Nilai Terakhir
Number_Dibalik = Credit_Number[::-1] # Index Dimulai Dari Nilai Paling Terakhir

print(Credit_Number[0]) # Index = [0], [1], [2], dst....nya
print(Credit_Number[0:4]) # Index = [Start : End]
print(Credit_Number[:4]) # Index = [Nilai Awal Credit_Number : End]
print(Credit_Number[5:9]) # Index = [Start : End]
print(Credit_Number[5:]) # Index = [Start : Nilai Terakhir Credit_Number]
print(Credit_Number[-1]) # Index = [Index Dimulai Dari Nilai Terakhir Credit_Number], [-2], [-3], [-4] dst.....nya
print(Credit_Number[::2]) # Index = [:: Step], Index Dimulai Dari Awal Kemudian Dengan Menghitung Step 2 Index
print()
print(f"XXXX-XXXX-XXXX-{Last_Digits}")
print()
print(Number_Dibalik)