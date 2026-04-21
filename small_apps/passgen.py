import random

eligible_signs = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
                  "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H",
                  "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y",
                  "Z", "1", "2", "3", "4", "5", "6", "7", "8","9", "0", "!", "§", "$", "%", "&", "/",
                  "(", ")", "?", "€", "@"]
random.shuffle(eligible_signs)

def passgen_part():
    password_part = []
    for sign in eligible_signs:
        checker = [1, 2, 3, 4, 5]
        check = random.choice(checker)
        if check == 1:
            password_part.append(sign)
            if len(password_part) == 6:
                break
    password_part.append("-")
    password_part_string = "".join(password_part)

    return password_part_string

# Start of the App

user_choice = input("Do you want to generate a password? (y/n): ")
if user_choice == "y":
    user_choice = True
else: user_choice = False

# Actual app running

if user_choice:
    password = ""
    for loop in range(5):
        password = password + passgen_part()
    password = password[:-1]
    print("Your password is:", password)
else: print("No password generated")


