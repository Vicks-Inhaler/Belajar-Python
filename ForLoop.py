# For Loops = Execute a block of code a fixed number of times.
#             You can iterate over a Range, String, Sequence, etc.

# ---------------------------------------------------
print()
for Counter in range (1, 11) :
    print(Counter)

# ---------------------------------------------------
print()
for Countdown in reversed(range (1, 11)) :
    print(Countdown)

print("HAPPY NEW YEARS!")

# ---------------------------------------------------
print()
for CountStep in range (1, 11, 2) : # (1, 11, 3), dst
    print(CountStep)

# ---------------------------------------------------
print()
Credit_Card = "1234-5678-9012-1470"

for X in Credit_Card :
    print(X)

# ---------------------------------------------------
print()
for Skip in range(1, 21) :
    if Skip == 13 :
        continue
    else :
        print(Skip)

# ---------------------------------------------------
print()
for Stop in range(1, 21) :
    if Stop == 13 :
        break
    else :
        print(Stop)