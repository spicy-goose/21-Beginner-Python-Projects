import random

def playNumberGuess(x):
    guessedCorrectly = False
    correctNumber = random.randint(0,x)
    currentGuess = int(input(f"Select a number between 0 and {x}: "))
    while guessedCorrectly == False:
        if currentGuess == correctNumber:
            guessedCorrectly = True
            continue
        if (currentGuess > correctNumber):
            currentGuess = int(input("Too high, try again: "))
            continue
        currentGuess = int(input("Too low, try again: "))
    print(f"Congrats! {correctNumber} was the right answer!")

def pcPlayNumberGuess(x):
    guessedCorrectly = False
    correctNumber = int(input(f"Select a number between 0 and {x}: "))
    lowBound = 0
    highBound = x
    
    while guessedCorrectly == False:
        currentGuess = random.randint(lowBound, highBound)
        if currentGuess == correctNumber:
            guessedCorrectly = True
            continue
        if (currentGuess > correctNumber):
            print(f'Computer picked {currentGuess}, it was too high')
            highBound = currentGuess-1
            continue
        print(f'Computer picked {currentGuess}, it was too low')
        lowBound = currentGuess+1
    print(f"Congrats Computer! {correctNumber} was the right answer!")

def decidePlayerGame():
    decision = input('what guessing game to play? player guess (1) or computer guess (2): ')
    rangeOfGame = int(input('How big do you want the number for the game?: '))
    if decision == "1":
        playNumberGuess(rangeOfGame)
        return
    pcPlayNumberGuess(rangeOfGame)

decidePlayerGame()