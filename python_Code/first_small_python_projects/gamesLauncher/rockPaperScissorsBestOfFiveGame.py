import random

def start():

    valid_options = ["schere", "stein", "papier", "exit"]
    user_choice = ""
    user_score, computer_score = 0, 0

    while user_choice != "Exit":
        if user_score >2:
            print("DU HAST DAS MATCH GEWONNEN")
            break
        elif computer_score > 2:
            print("DU HAST DAS MATCH LEIDER VERLOREN")
            break

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

        wins_against = {
            "Schere": "Papier",
            "Stein":  "Schere",
            "Papier": "Stein",
        }

        if user_choice == "Exit":
            print()
        elif user_choice == computer_choice:
            print("Unentschieden")
        elif wins_against[user_choice] == computer_choice:
            print("Du hast gewonnen :)")
            user_score += 1
        else:
            print("Du hast verloren :(")
            computer_score += 1

        print("--------")
        print("Score:")
        print(f"Du: {user_score}; Com: {computer_score}")

if __name__ == "__main__":
    start()