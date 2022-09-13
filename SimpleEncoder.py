import random
import os
import math
from sqlite3 import apilevel

#ask for a word or phrase
#shift each letter (even space) by one or two characters

def clear(): os.system('cls') #This clears the console so that the user has a better exerience

alphabet = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ".", ",", "!", "?", "/", "<", ">"]

def Continue():
    choice = input("Do you want to continue?\n")

    if choice.lower() == "yes" or choice.lower() == "y":
        Start()

    else:
        clear()

def Scramble():
    clear()

    phraseCharList = ""

    phrase = input("Type a word or phrase to encode.\n")

    scrambleNum = int(input("By how many places do you want to scramble this word/phrase?\n"))

    while scrambleNum >= len(alphabet):
        scrambleNum -= len(alphabet)

    for x in phrase:
        locationNum = alphabet.index(x.lower())

        newLocationNum = locationNum + scrambleNum

        if newLocationNum > len(alphabet):
            newLocationNum -= len(alphabet)

        if alphabet[locationNum].upper() == x:
            phraseCharList += alphabet[newLocationNum].upper()

        else:
            phraseCharList += alphabet[newLocationNum]

    print(phrase)
    print(phraseCharList)

    Continue()

def UnScramble():
    clear()

    phrase = input("What word or phrase to you want to decode?\n")

    i = 1

    while i <= len(alphabet):
        unScrambledPhrase = ""

        for x in phrase:
            locationNum = alphabet.index(x.lower())

            newLocationNum = locationNum + i

            if newLocationNum >= len(alphabet):
                newLocationNum -= len(alphabet)

            unScrambledPhrase += alphabet[newLocationNum]

        print(str(unScrambledPhrase + "\n"))
        
        i += 1

    Continue()
    
def Start():
    clear()

    choice = input("Do you want to encode (1) or decode (2)?\n")

    if choice == "1":
        Scramble()

    elif choice == "2":
        UnScramble()

    else:
        Start()

Start()



