import random
from sqlite3 import Cursor
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

def displayCurrentScore(numberOfLives, currentWordGuess, allLetterArray):
    print(f"Current number of lives: {numberOfLives}\
    Letters used: {allLetterArray}\
    Word: {currentWordGuess}")
    print("\n") #new line for aesthetic purposes
    return

def playHangman():
    numberOfLives = 5
    selectedWord = getValidWord(words)
    correctWord = list(selectedWord)
    currentWordGuess = list("-" * len(correctWord)) #creates empty initial guess using dashes
    currentLetterGuess = ""
    allLetterArray = []
    
    print("Let's play Hangman")
    displayCurrentScore(numberOfLives, currentWordGuess, allLetterArray)

    while currentWordGuess != correctWord:

        if numberOfLives < 1:
            break

        currentLetterGuess = input("What letter is your guess? ")
        print("\n") #new line for aesthetic purposes

        if (letterIsInWord(currentLetterGuess, selectedWord) == False):
            numberOfLives -= 1
            allLetterArray.append(currentLetterGuess)
            print(f"Sorry, {currentLetterGuess} is not in the word")
            displayCurrentScore(numberOfLives, currentWordGuess, allLetterArray)
            continue
        
        elif (wordHasDuplicateLetters(currentLetterGuess, selectedWord) == False):
            allLetterArray.append(currentLetterGuess)
            currentWordGuess[selectedWord.find(currentLetterGuess)] = currentLetterGuess
            print(f'Bingo! {currentLetterGuess} is correct!')
            displayCurrentScore(numberOfLives, currentWordGuess, allLetterArray)
            continue

        indexes = findIndexOfDuplicates(currentLetterGuess, selectedWord)
        for i in indexes:
            currentWordGuess[i] = currentLetterGuess
            
        allLetterArray.append(currentLetterGuess)    
        print(f'Bingo! {currentLetterGuess} is correct!')    
        displayCurrentScore(numberOfLives, currentWordGuess, allLetterArray)

    if (numberOfLives < 1):
        print(f"Sorry, you lose. The word we were looking for is '{selectedWord}'!")
        return

    print(f"Congrats! '{selectedWord}' is the correct word!")        

playHangman()
