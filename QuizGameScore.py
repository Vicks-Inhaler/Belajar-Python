# Python Quiz Game

print()
Questions = ("How Many Element Are In The Periodic Table? : ",
            "Which Animal Lays The Largest Eggs? : ",
            "What Is The Most Abundant Gas In Earth's Atmosphere? : ",
            "How Many Bones Are In The Human Body? : ",
            "Which Planet In The Solar System Is The Hottest? : ")

Options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

Answers = ("C", "D", "A", "A", "B")
Guesses = []
Score = 0
Question_Num = 0

for Question in Questions :
    print(Question)
    for Option in Options[Question_Num] :
        print(Option)
    print("--------------------------------------------------------")

    Guess = input("Enter (A, B, C, D) : ").upper()
    Guesses.append(Guess)
    if Guess == Answers[Question_Num] :
        Score += 1
        print("CORRECT!")
        print("Good Job!")
        print("========================================================")
    else :
        print("INCORRECT!")
        print("You Are Stupid!")
        print(f"{Answers[Question_Num]} Is The Correct Answer")
        print("========================================================")
    Question_Num += 1

print()
print("--------------------")
print("       RESULT       ")
print("--------------------")

print("Answers : ", end="")
for Answer in Answers :
    print(Answer, end=" ")
print()

print("Guesses : ", end="")
for Guess in Guesses :
    print(Guess, end=" ")
print()

Score = int(Score / len(Questions) * 100)
print(f"Your Score Is : {Score}%")