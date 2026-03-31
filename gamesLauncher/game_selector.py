import coinflipGame
import coinflipBestOfFiveGame
import rockPaperScissorsGame
import rockPaperScissorsBestOfFiveGame


print("Folgendes ist spielbar:")
print("1: CoinFlip")
print("2: CoinFlip Best of Five")
print("3: RockPaperScissors")
print("4: RockPaperScissors Best of Five")
choice = input("Wähle dein Spiel aus >> ")

games = {
    "1": coinflipGame.start,
    "2": coinflipBestOfFiveGame.start,
    "3": rockPaperScissorsGame.start,
    "4": rockPaperScissorsBestOfFiveGame.start
}






print("Fertig.")
