# Game Dadu 1-6

import random

print()
print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

Dices_Art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

print()
Dices = []
Total = 0
Num_Of_Dices = int(input("How Many Dice? : "))

# -----------------------------------------------------------
for Dice in range(Num_Of_Dices) :
    Dices.append(random.randint(1, 6))

print(Dices)

# -----------------------------------------------------------
# for Dice in range(Num_Of_Dices) :
    # for Line in Dices_Art.get(Dices[Dice]) :
        # print(Line)

# Atau Program Singkatnya =
for Line in range(5) :
    for Dice in Dices :
        # print(Dices_Art.get(Dice)[Line])              # Tampilan akhirnya Sejajar dan Menumpuk
        print(Dices_Art.get(Dice)[Line], end="")        # Tampilan Sudah Sebaris terpisah Belum Terlihat Seperti Dadu
    print()                                             # Pemisah antar baris ke bawahnya agar terbentuk seperti Dadu

# -----------------------------------------------------------
for Dice in Dices :
    Total += Dice
print(f"Total : {Total}")