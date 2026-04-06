# pls fix

import random

user_choice = input("Do you want to generate a password? (y/n): ")
if user_choice == "y":
    user_choice = True
else: user_choice = False

if user_choice:
    eligible_signs = "abcdefghijklmnopqrstuvwxyz"
    password = ""
    print(len(eligible_signs))



