# Random Number like Dadu

import random

print()
#print(help(random))

Low = 1
High = 100
Options = ("Rock", "Paper", "Scissors")
Cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "AS"]

Number = random.randint(1, 6)                       # Nilai Random 1-6 setiap sekali program dijalankan
Number1 = random.randint(1, 20)                     # Nilai Random 1-20 setiap sekali program dijalankan
Number2 = random.randint(Low, High)
Number3 = random.random()
Options = random.choice(Options)
random.shuffle(Cards)
Card = random.shuffle(Cards)

print(Number)
print(Number1)
print(Number2)
print(Number3)
print(Options)
print(Cards)
print(Card)
