from mimetypes import guess_extension
from random import random


import random

def playNumberGuess():
    guessedCorrectly = False
    correctNumber = random.randint(0,10)
    currentGuess = int(input("Select a number between 0 and 10: "))
    while guessedCorrectly == False:
        if currentGuess == correctNumber:
            guessedCorrectly = True
            continue
        if (currentGuess > correctNumber):
            currentGuess = int(input("Too high, try again: "))
            continue
        currentGuess = int(input("Too low, try again: "))
    print(f"Congrats! {correctNumber} was the right answer!")

playNumberGuess()