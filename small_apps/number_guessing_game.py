solution = 42

def game(user_input):
    while user_input != solution:
        if user_input > solution:
            user_input = int(input("Too high! Guess again: "))
        elif user_input < solution:
            user_input = int(input("Too low! Guess again: "))


wanna_play = "yes"

while wanna_play == "yes":
    initial_input = int(input("I'm thinking of a number! Try to guess the number I'm thinking of: "))
    game(initial_input)
    wanna_play = input("That's it! Would you like to play again? (yes/no): ")


print("Thanks for playing!")