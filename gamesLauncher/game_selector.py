import coinflipGame
import coinflipBestOfFiveGame
import rockPaperScissorsGame
import rockPaperScissorsBestOfFiveGame


print("""Folgendes ist spielbar:
1: CoinFlip
2: CoinFlip Best of Five
3: RockPaperScissors
4: RockPaperScissors Best of Five""")

choice = input("Wähle dein Spiel aus >> ")

games = {
    "1": coinflipGame.start,
    "2": coinflipBestOfFiveGame.start,
    "3": rockPaperScissorsGame.start,
    "4": rockPaperScissorsBestOfFiveGame.start
}

if choice in games:
    games[choice]()
else: print("Spiel wurde nicht gefunden. Programm wird beendet.")


print("Fertig.")
