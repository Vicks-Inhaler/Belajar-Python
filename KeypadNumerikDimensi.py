# Program Keypad Numerik

print()
Num_Pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for Row in Num_Pad :
    print(Row)

print()
for Row in Num_Pad :
    for Num in Row :
        # print(Num)                # Mapping Tiap Index Turun Ke Bawah Or
        print(Num, end=" ")         # Sejajar Kesamping Dengan Spasi
    print()                         # Untuk Memisahkan Ke Bawah Menjadi Setiap Array Index Data