# Format Specifiers = {value:flags} format a value based on what flags are inserted

# .(Number)f = Round to that many decimal places (Fixed Point)
# :(Number)f = Allocate that many spaces
# :03 = Allocate and zero pad that many spaces
# :< = Letf Justify
# :> = Right Justify
# :^ = Center Align
# :+ = Use a plus sign to indicate positive value
# := = Place sign to leftmost position
# : = Insert a space before positive numbers
# :, = Comma separator

Price1 = 3.14159
Price2 = -987.65
Price3 = 12.34

# .(Number)f = Round to that many decimal places (Fixed Point)
# ------------------------------------------------------------
print()
print(f"Price 1 Is ${Price1:.1f}")
print(f"Price 2 Is ${Price2:.1f}")
print(f"Price 3 Is ${Price3:.1f}")
print()
print(f"Price 1 Is ${Price1:.2f}")
print(f"Price 2 Is ${Price2:.2f}")
print(f"Price 3 Is ${Price3:.2f}")

# :(Number)f = Allocate that many spaces
# ------------------------------------------------------------
print()
# 10 Character setelah $ dengan spasi => ($   3.14159)
print(f"Price 1 Is ${Price1:10}")
print(f"Price 2 Is ${Price2:10}")
print(f"Price 3 Is ${Price3:10}")
print()

# :03 = Allocate and zero pad that many spaces
# ------------------------------------------------------------
print()
# 10 Character setelah $ dimana spasi diganti dengan angka 0 => Contoh ($0003.14159)
print(f"Price 1 Is ${Price1:010}")
print(f"Price 2 Is ${Price2:010}")
print(f"Price 3 Is ${Price3:010}")

# :< = Letf Justify
# ------------------------------------------------------------
print()
# 10 Character setelah $ => dimana spasi terletak setelah Angka terakhir ($3.14159   )
print(f"Price 1 Is ${Price1:<10}")
print(f"Price 2 Is ${Price2:<10}")
print(f"Price 3 Is ${Price3:<10}")

# :> = Right Justify
# ------------------------------------------------------------
print()
# 10 Character setelah $ => dimana spasi terletak Diawal Angka ($   3.14159)
print(f"Price 1 Is ${Price1:>10}")
print(f"Price 2 Is ${Price2:>10}")
print(f"Price 3 Is ${Price3:>10}")

# :^ = Center Align
# ------------------------------------------------------------
print()
# 10 Character setelah $ => dimana Angka terletak Ditengah2 Spasi ($ 3.14159  )
print(f"Price 1 Is ${Price1:^10}")
print(f"Price 2 Is ${Price2:^10}")
print(f"Price 3 Is ${Price3:^10}")

# :+ = Use a plus sign to indicate positive value
# ------------------------------------------------------------
print()
# Untuk Menentukan Nilai Tersebut Bernilai Positif atau Negatif ($+3.14159, $-987.65, $+12.34)
print(f"Price 1 Is ${Price1:+}")
print(f"Price 2 Is ${Price2:+}")
print(f"Price 3 Is ${Price3:+}")

# := = Place sign to leftmost position
# ------------------------------------------------------------
print()
# Untuk Menentukan Nilai Tersebut Bernilai Positif atau Negatif
# Tanpa Spasi jika bernilai postitif ($3.14159, $-987.65, $12.34)
print(f"Price 1 Is ${Price1:=}")
print(f"Price 2 Is ${Price2:=}")
print(f"Price 3 Is ${Price3:=}")

# : = Insert a space before positive numbers
# ------------------------------------------------------------
print()
# Jika Nilai Tersebut Bernilai Positif Maka Setelah $ Ditambah Spasi
# Apabila Negatif Tidak ($ 3.14159, $-987.65, $ 12.34)
print(f"Price 1 Is ${Price1: }")
print(f"Price 2 Is ${Price2: }")
print(f"Price 3 Is ${Price3: }")

# :, = Comma separator
# ------------------------------------------------------------
Price1 = 3000.14159
Price2 = -9870.65
Price3 = 1200.34

print()
# Menentukan Nilai Ribuan Pada Angka Bulat Didepan Koma Setelah $ => ($3,000.14159, $-9,870.65, $1,200.34)
print(f"Price 1 Is ${Price1:,}")
print(f"Price 2 Is ${Price2:,}")
print(f"Price 3 Is ${Price3:,}")

print()
# Menentukan Nilai Ribuan Pada Angka Bulat Didepan Koma Setelah $
# Dan 2 digit angka desimal dibelakang koma => ($3,000.14, $-9,870.65, $1,200.34)
print(f"Price 1 Is ${Price1:,.2f}")
print(f"Price 2 Is ${Price2:,.2f}")
print(f"Price 3 Is ${Price3:,.2f}")

print()
# Menentukan Nilai Positif/Negatif Ribuan Pada Angka Bulat Didepan Koma Setelah $
# Dan 2 digit angka desimal dibelakang koma => ($3,000.14, $-9,870.65, $1,200.34)
print(f"Price 1 Is ${Price1:+,.2f}")
print(f"Price 2 Is ${Price2:+,.2f}")
print(f"Price 3 Is ${Price3:+,.2f}")