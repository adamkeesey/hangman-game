"""
Simple CLI hangman written in procedural python
Author: Adam Keesey
"""

import os
import random
import sys

TOTAL_LIVES = 7

with open("wordlist.txt") as f:
    WORDS = f.readlines()

CORRECT_GUESSES = []
INCORRECT_GUEESES = []


def main():
    """ Main running program """

    lives = TOTAL_LIVES

    word = random.choice(WORDS)
    word = word.lower().strip()

    while True:
        if lives:
            lives = play(word, lives)
        else:
            print("\U0001f61e GAME OVER!")
            print("The correct answer was", word)
            sys.exit()


def play(word, lives):
    """ Play the hangman game """

    os.system("clear")
    print("The word is {} letters long".format(len(word)))
    print("You have {} lives left".format(lives))

    lives_output = ""
    for i in range(TOTAL_LIVES):
        if i >= len(INCORRECT_GUEESES):
            lives_output += "\U0001f49a"
        else:
            lives_output += "\U0001f494"

    print(lives_output)
    print("Incorrect Choices: {}".format(INCORRECT_GUEESES))

    output = ""
    for letter in word:
        if letter in CORRECT_GUESSES:
            output += letter + " "
        else:
            output += "_ "

    if "_" not in output:
        print(word)
        print("\U0001f44d WOHOOOOOOO YOU WON!")
        sys.exit()

    print(output)

    choice = input('\nPlease enter a letter: ')

    if len(choice) > 1:
        print("Please only enter one letter!")
        return lives

    if choice in CORRECT_GUESSES or choice in INCORRECT_GUEESES:
        return lives

    if choice in word:
        CORRECT_GUESSES.append(choice)
    else:
        lives -= 1
        INCORRECT_GUEESES.append(choice)

    return lives


if __name__ == "__main__":
    main()
