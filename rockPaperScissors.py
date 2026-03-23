import random

valid_options = ["schere", "stein", "papier", "exit"]

while True:
    user_choice = input("Wähle Schere, Stein oder Papier >> ")
    if user_choice.lower() in valid_options:
        break
    else: print("Schreibfehler! Probiers nochmal.")


user_choice = user_choice.capitalize()
computer_choice = random.choice(["Schere", "Stein", "Papier"])

if user_choice == "Exit":
    print("Du hast das Programm verlassen.")
    exit()

print("Deine Auswahl: ", user_choice)
print("Computer Auswahl: ", computer_choice)

#Scoring

if user_choice == "Exit":
    print()
elif user_choice == computer_choice:
    print("Unentschieden")
elif user_choice == "Papier" and computer_choice == "Schere":
    print("Du hast verloren :(")
elif user_choice == "Papier" and computer_choice == "Stein":
    print("Du hast gewonnen :)")
elif user_choice == "Schere" and computer_choice == "Stein":
    print("Du hast verloren :(")
elif user_choice == "Schere" and computer_choice == "Papier":
    print("Du hast gewonnen :)")
elif user_choice == "Stein" and computer_choice == "Papier":
    print("Du hast verloren :(")
elif user_choice == "Stein" and computer_choice == "Schere":
    print("Du hast gewonnen :)")
