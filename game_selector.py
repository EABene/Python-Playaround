import coinflip

print("Folgendes ist spielbar \n 1: Coinflip")
user_input = input("Wähle dein Spiel aus: ")

if user_input == "1":
    coinflip.main()

print("Fertig.")
