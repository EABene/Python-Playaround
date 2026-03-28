import random


user_score, computer_score = 0, 0

while user_score < 3 and computer_score < 3:

    user_input = input("Wähle Kopf oder Zahl: >> ")
    computer_input = random.choice(["Kopf", "Zahl"])

    print("Du sagst:", user_input)
    print("Münzwurf:", computer_input)

    if user_input == computer_input:
        user_score += 1             # wenn richtig
    else: computer_score += 1       # wenn falsch

    if user_score > 2:
        print("Gratuliere, du hast gewonnen!")
    elif computer_score > 2: print("Leider verloren...")

    if user_score < 3 and computer_score < 3:
        print("Zwischenstand:")
        print(f"Du: {user_score}, Computer: {computer_score}")