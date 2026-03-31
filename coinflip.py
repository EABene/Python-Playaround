import random
import sys


user_input = input("Wähle Kopf oder Zahl: >> ")
user_input = user_input.capitalize()
computer_input = random.choice(["Kopf", "Zahl"])


if user_input == "Aufgeben":
    print("Du hast Aufgegeben. Kein Spiel")
    sys.exit()

print("Du sagst:", user_input)
print("Münzwurf:", computer_input)

if user_input == computer_input:
    print("Congrats, you win!")
else: print("Unlucky, you lost...")
