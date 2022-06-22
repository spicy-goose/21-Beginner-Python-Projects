import random
from words import words

def getValidWord(wordlist):
    indexSelection = random.randint(0, len(wordlist)-1)
    wordSelection = wordlist[indexSelection]
    if len(wordSelection) > 3:
        return wordSelection

    return getValidWord(wordlist)

def letterIsInWord(letter, word):
    return letter in word

def wordHasDuplicateLetters(letter, word):
    return word.find(letter) != word.rfind(letter)

def findIndexOfDuplicates(letter, word):
    indexes = []
    indexOfLetter = 0
    while True:
        indexOfLetter = word.find(letter, indexOfLetter) #finds next index of letter
        if indexOfLetter == -1:
            break
        indexes.append(indexOfLetter)
        indexOfLetter += 1
    return indexes

def display(numberOfLives, correctWord, currentWordGuess, allLetterArray):
    print(f"Current number of lives: {numberOfLives}/n\
    Letters used: {allLetterArray}/n\
    Word: ")

def playHangman():
    numberOfLives = 5
    correctWord = getValidWord(words).split("")
    currentWordGuess = ("-" * len(correctWord)).split("") #creates empty initial guess using dashes
    currentLetterGuess = ""
    allLetterArray = []

    while currentWordGuess != correctWord:
        currentLetterGuess = input("What letter is your guess? /n")
        if (letterIsInWord(currentLetterGuess) == False):
            numberOfLives -= 1
            allLetterArray.append(currentLetterGuess)
            print(f"Sorry, {currentLetterGuess} is not in the word")

print(["a"] == ["a"])