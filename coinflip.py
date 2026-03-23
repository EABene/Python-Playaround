import random

user_input = input("Wähle Kopf oder Zahl: >> ")
computer_input = random.choice(["Kopf", "Zahl"])

print("Your input:", user_input)
print("Computer input:", computer_input)

if user_input == computer_input:
    print("Congrats, you win!")
else: print("Unlucky, you lost...")
