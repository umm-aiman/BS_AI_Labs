# -*- coding: utf-8 -*-
"""Lab5_pwai0009.py

"""

attempts = 5
password_is_strong = False

while attempts > 0:
    password = input(f"Enter your password: ")
    length_check = len(password) >= 8
    digit_check = any(char.isdigit() for char in password)
    uppercase_check = any(char.isupper() for char in password)

    conditions_met = sum([length_check, digit_check, uppercase_check])
    feedback = ""
    if conditions_met == 0:
        feedback = "Very Weak"
    elif conditions_met == 1:
        feedback = "Weak"
    elif conditions_met == 2:
        feedback = "Normal"
    else:
        feedback = "Strong"

    print(f"Password strength: {feedback}")

    if feedback == "Strong":
        print(f"You created a strong password!")
        password_is_strong = True
        break

    attempts -= 1
    if attempts > 0:
        print(f"Remaining attempts: {attempts}")
if not password_is_strong:
    print(f"Final Result: Password is not strong.")

