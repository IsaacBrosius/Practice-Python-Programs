import random
import os
import math


playedGoodBotTimes = 0
playedBetterBotTimes = 0

def clear(): os.system('cls') #This clears the console so that the user has a better exerience

def funnyNumberFinder(number):
    if number == 69 or number == 420:
        print("Nice.")

    if number == 42:
        print("I've been told that that is the meaning of life.")

def NumberGuesserIsHuman():
    clear()

    numberToGuess = random.randint(1, 100)

    global playing
    playing = True

    guessNum = 0

    while playing == True:

        guess = int(input("Guess:\n"))

        if guess > numberToGuess:
            funnyNumberFinder(guess)

            print("Lower\n")

            guessNum += 1

        elif guess < numberToGuess:
            funnyNumberFinder(guess)

            print("Higher\n")

            guessNum += 1

        elif guess == numberToGuess:

            guessNum += 1

            print("You guessed it!")

            funnyNumberFinder(guess)

            print(f"\nTotal guesses: {guessNum}")
            print("The par is 8.\n")

            print("Play again?")

            answer = input()

            if answer.lower() == "yes" or answer.lower() == "y":
                GameType()

            elif answer.lower() == "no" or answer.lower() == "n":
                print("I'm sad to see you go. Good bye.")

                playing = False

def GoodBot():

    def NotAuto():
        clear()

        high = 100
        low = 1
        feedback = ""
        guessNum = 0

        while (feedback.lower() != "c" and feedback.lower() != "correct"):
            if (low != high):
                try:
                    guess = random.randint(low, high)
                except:
                    guess = low
            else: 
                guess = low

            print(guess)

            funnyNumberFinder(guess)

            feedback = input()

            clear()

            if feedback.lower() == "high" or feedback.lower() == "h":
                high = guess - 1
                guessNum += 1

            elif feedback.lower() == "low" or feedback.lower() == "l":
                low = guess + 1
                guessNum += 1

        guessNum += 1

        global playedGoodBotTimes
        playedGoodBotTimes += 1

        clear()
        
        print(f"The Good Bot guessed it in {guessNum} tries!\n")

        answer = input("Do you want to keep playing?\n")

        if answer.lower() == "yes" or answer.lower() == "y":
            GameType()

    def Auto():
        high = 100
        low = 1
        guessNum = 0
        guess = 0

        number = int(input("What's the number (1 - 100)?\n"))

        clear()

        while guess != number:
            guess = random.randint(low, high)
            if guess > number:
                high = guess -1
                guessNum += 1

            elif guess < number:
                low = guess + 1
                guessNum += 1

            print(guess)

            funnyNumberFinder(guess)

        guessNum += 1

        global playedGoodBotTimes
        playedGoodBotTimes += 1
        
        print(f"\nThe Good Bot guessed it in {guessNum} tries!\n")

        answer = input("Do you want to keep playing?\n")

        if answer.lower() == "yes" or answer.lower() == "y":
            GameType()

    clear()

    if playedGoodBotTimes == 0:
        print("Think of a number from 1 - 100.")

        print("Type 'high' if the computer guesses too high, 'low' if it guesses too low, and 'correct' if it guesses correctly.")

        ready = input("Type 'ready' when you are ready.\n")

        if ready.lower() == "ready" or ready.lower() == "y":
            NotAuto()

        else:
            GoodBot()

    elif playedGoodBotTimes >= 1:
        if playedGoodBotTimes == 1:
            print("You have unlocked the 'auto' mode. In 'auto' mode, you type your number and the computer tries to guess it in as few guesses as possible")

            print("without having to ask you if it's higher or lower.\n")

        ready = input("Type 'auto' if you want to do the 'auto' mode. Type 'ready' if you want to play the regular mode.\n")

        if ready.lower() == "ready" or ready.lower() == "y":
            NotAuto()

        elif ready.lower() == "auto" or ready.lower() == "a":
            Auto()

        else:
            GoodBot()

def BetterBot():

    def Auto():
        clear()

        high = 100
        low = 1
        guessNum = 0
        guess = 0

        number = int(input("What's the number (1 - 100)?\n"))

        while guess != number:
            if (low != high):
                guess = int(math.ceil(high - ((high - low) / 2)))
            else: 
                guess = low

            print(guess)

            funnyNumberFinder(guess)

            if guess > number:
                high = guess - 1
                guessNum += 1

            elif guess < number:
                low = guess + 1
                guessNum += 1

        guessNum += 1

        global playedBetterBotTimes
        playedBetterBotTimes += 1
        
        print(f"The Better Bot guessed it in {guessNum} tries!\n")

        answer = input("Do you want to keep playing?\n")

        if answer.lower() == "yes" or answer.lower() == "y":
            GameType()

        else: 
            clear()

    def NotAuto():
        clear()

        high = 100
        low = 1
        feedback = ""
        guessNum = 0

        while (feedback.lower() != "c" and feedback.lower() != "correct"):
            if (low != high):
                guess = int(math.ceil(high - ((high - low) / 2)))
            else: 
                guess = low

            print(guess)
            funnyNumberFinder(guess)

            feedback = input()

            clear()

            if feedback.lower() == "high" or feedback.lower() == "h":
                high = guess - 1
                guessNum += 1

            elif feedback.lower() == "low" or feedback.lower() == "l":
                low = guess + 1
                guessNum += 1

        guessNum += 1

        global playedBetterBotTimes
        playedBetterBotTimes += 1

        clear()
        
        print(f"The Better Bot guessed it in {guessNum} tries!\n")

        answer = input("Do you want to keep playing?\n")

        if answer.lower() == "yes" or answer.lower() == "y":
            GameType()

    clear()

    if playedBetterBotTimes == 0:
        print("Think of a number from 1 - 100.")

        print("Type 'high' if the computer guesses too high, 'low' if it guesses too low, and 'correct' if it guesses correctly.")

        ready = input("Type 'ready' when you are ready.\n")

        if ready.lower() == "ready" or ready.lower() == "y":
            NotAuto()

        else:
            GoodBot()

    elif playedBetterBotTimes >= 1:
        if playedBetterBotTimes == 1:
            print("You have unlocked the 'auto' mode. In 'auto' mode, you type your number and the computer tries to guess it in as few guesses as possible")

            print("without having to ask you if it's higher or lower.\n")

        ready = input("Type 'auto' if you want to do the 'auto' mode. Type 'ready' if you want to play the regular mode.\n")

        if ready.lower() == "ready" or ready.lower() == "y":
            NotAuto()

        elif ready.lower() == "auto" or ready.lower() == "a":
            Auto()

        else:
            BetterBot()

def GameType():
    clear()

    gameType = int(input("What game do you want to play? You could guess a number (1), or have the computer guess a number (2).\n"))

    if gameType == 1:

        answer = input("You have to guess a number 1 - 100. Are you ready? The record is 4, btw.\n")

        clear()

        if answer.lower() == "yes" or answer.lower() == "y":
            NumberGuesserIsHuman()

        elif answer.lower() == "no" or answer.lower() == "n":
            print("How can you not be ready for something like this?")

    elif gameType == 2:
        clear()

        print("Computer guesses.\n")

        skillLevel = int(input("How good should the computer be? Good (1), or really good (2)?\n"))

        if skillLevel == 1:
            GoodBot()

        elif skillLevel == 2:
            BetterBot()

def NumberGuesserStart():
    clear()

    playGameAnswer = input("Do you want to play a little game?\n")

    clear()

    if playGameAnswer.lower() == "yes" or playGameAnswer.lower() == "y":

        GameType()

    elif playGameAnswer.lower() == "no" or playGameAnswer.lower() == "n":
        print("Then why are you here?")

NumberGuesserStart()