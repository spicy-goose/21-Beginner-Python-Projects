import random
from sqlite3 import Cursor
from words import words
import string

def getValidWord(wordlist):
    indexSelection = random.randint(0, len(wordlist)-1)
    wordSelection = wordlist[indexSelection]
    if len(wordSelection) > 3:
        return wordSelection

    return getValidWord(wordlist)

def letterIsInWord(letter, word):
    return letter in word

def displayCurrentScore(numberOfLives, selectedWord, allLettersUsedSet):
    currentWord = [letter if letter in allLettersUsedSet else "-" for letter in selectedWord]
    print(f"Current number of lives: {numberOfLives}\
    Letters used: {allLettersUsedSet}\
    Word: {currentWord}")
    print("\n") #new line for aesthetic purposes
    return

def playHangman():

    numberOfLives = 5
    selectedWord = getValidWord(words)
    correctWord = set(selectedWord)
    currentLetterGuess = ""
    allLettersUsedSet = set()
    alphabet = set(string.ascii_lowercase)

    print("Let's play Hangman")

    while len(correctWord) > 0 and numberOfLives > 0:

        displayCurrentScore(numberOfLives, selectedWord, allLettersUsedSet)
        currentLetterGuess = input("What letter is your guess? ").lower()
        print("\n") #new line for aesthetic purposes

        if len(currentLetterGuess) > 1 or currentLetterGuess not in alphabet:
            print("Invalid guess, Try again!")
            continue
        elif currentLetterGuess in allLettersUsedSet:
            print(f'You already used {currentLetterGuess}, try again!')
            continue

        allLettersUsedSet.add(currentLetterGuess)

        if (letterIsInWord(currentLetterGuess, selectedWord) == False):
            numberOfLives -= 1
            print(f"Sorry, {currentLetterGuess} is not in the word")
            continue
        
        correctWord.remove(currentLetterGuess)
        print(f'Bingo! {currentLetterGuess} is correct!')
            

    if (numberOfLives < 1):
        print(f"Sorry, you lose. The word we were looking for is '{selectedWord}'!")
        return

    print(f"Congrats! '{selectedWord}' is the correct word!")        

playHangman()
