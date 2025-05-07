print()
import time

# --------------------------------------------
time.sleep(3)

print("TIME'S UP!")

# --------------------------------------------
print()
My_Time = int(input("Enter The Time In Seconds (Display Counter) : "))

for Counter in range (0, My_Time) :
    print(Counter)
    time.sleep(1) # 1 Seconds

print("TIME'S UP!")

# --------------------------------------------
print()
My_Time = int(input("Enter The Time In Seconds (Display Countdown) : "))

for Countdown in reversed(range(0, My_Time)) :
    print(Countdown)
    time.sleep(1) # 1 Seconds

print("TIME'S UP!")

# --------------------------------------------
print()
My_Time = int(input("Enter The Time In Seconds (Display Countdown) : "))

for Countdown in range(My_Time, 0, -1) :
    print(Countdown)
    time.sleep(1) # 1 Seconds

print("TIME'S UP!")

# --------------------------------------------
print()
My_Time = int(input("Enter The Time In Seconds (Display 1 Digit Seconds) : "))

for Countdown in range(My_Time, 0, -1) :
    Seconds = Countdown % 60
    print(f"00:00:{Seconds}")
    time.sleep(1) # 1 Seconds

print("TIME'S UP!")

# Seconds Change
# --------------------------------------------
print()
My_Time = int(input("Enter The Time In Seconds (Display 2 Digit Second) : "))

for Countdown in range(My_Time, 0, -1) :
    Seconds = Countdown % 60
    print(f"00:00:{Seconds:02}")
    time.sleep(1) # 1 Seconds

print("TIME'S UP!")

# Minutes Change
# --------------------------------------------
print()
My_Time = int(input("Enter The Time In Seconds (Display 2 Digit MinuteSecond) : "))

for Countdown in range(My_Time, 0, -1) :
    Seconds = Countdown % 60
    Minutes = int(Countdown / 60) % 60
    print(f"00:{Minutes:02}:{Seconds:02}")
    time.sleep(1) # 1 Seconds

print("TIME'S UP!")

# Hours 24 Jam Change
# --------------------------------------------
print()
My_Time = int(input("Enter The Time In Seconds (Display 2 Digit Hour MinuteSecond) : "))

for Countdown in range(My_Time, 0, -1) :
    Seconds = Countdown % 60
    Minutes = int(Countdown / 60) % 60
    Hours = int(Countdown / 3600)
    print(f"{Hours:02}:{Minutes:02}:{Seconds:02}")
    time.sleep(1) # 1 Seconds

print("TIME'S UP!")

# Hours 24 Jam Change
# --------------------------------------------
print()
My_Time = int(input("Enter The Time In Seconds (Display 2 Digit 24 Hour MinuteSecond) : "))

for Countdown in range(My_Time, 0, -1) :
    Seconds = Countdown % 60
    Minutes = int(Countdown / 60) % 60
    Hours = int(Countdown / 3600) % 24
    print(f"{Hours:02}:{Minutes:02}:{Seconds:02}")
    time.sleep(1) # 1 Seconds

print("TIME'S UP!")