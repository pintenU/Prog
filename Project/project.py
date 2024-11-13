"""
FILNAMN.PY: Project genom Python

author  = "Alexander Pintér"
version = "1.0.0"
email   = "Alexander.pinter@elev.ga.ntig.se"
"""
import random
import os
os.system("cls")

the_random_number = 0

while True:

    the_random_number = random.randint(1, 100)
    your_guess = 0
    remaining_tries = 7

    print("" * 6, "-" * 40)
    print("" * 6, "-" * 5, "GISSA NUMMRET MELLAN 1 - 100", "-" * 5)
    print("" * 6, "-" * 40, "\n")

    while remaining_tries > 0:

        try:
            your_guess = int(input("Vad vill du gissa på mellan 1-100? "))

        except:
            print("snälla snälla snälla snälla använd bara nummer mellan 1 - 100 ")
            continue

        if your_guess > 100:
            print("Snälla använd nummer inom 1 - 100 ")

        elif your_guess <= 0:
            print("Snälla använd nummer inom 1 - 100 ")

        if your_guess > the_random_number:
            remaining_tries -= 1
            print(f"Du har {remaining_tries} försök kvar \nDu gissade för högt")

        elif your_guess < the_random_number:
            remaining_tries -= 1
            print(f"Du har {remaining_tries} försök kvar \nDu gissade för lågt")

        if your_guess == the_random_number:
            print(f"Yipee du gissade rätt med {remaining_tries} försök kvar")
            break

    repeat_game = input("Vill du spela igen skriv 'j' eller 'n' om du vill avsluta: ")
    if repeat_game.upper()=="N":
        exit()




















