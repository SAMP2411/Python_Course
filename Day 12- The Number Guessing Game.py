logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""

# # my  method of solving the problem given
# import random


# def checkNum(guess, n, attempts):
#     if guess > n:
#         print("Too high")
#         return attempts - 1
#     elif guess < n:
#         print("Too low")
#         return attempts - 1
#     else:
#         return attempts


# print("Welcome to the Number Guessing Game!")
# print("I'm thinking of a number between 1 to 100.")

# difficulty = input("Choose a difficulty. Type 'easy' or 'hard' : ")
# num = random.randint(1, 100)

# if difficulty == "easy":
#     attempts = 10
# elif difficulty == "hard":
#     attempts = 5

# flag = True

# while flag:
#     print(f"You have {attempts} attempts remaining to guess the number.")
#     guessNum = int(input("Make a guess: "))
#     attempts = checkNum(guessNum, num, attempts)

#     if attempts == 0:
#         flag = False
#         print("You have run out of guesses, you Lose.")
#     elif guessNum == num:
#         flag = False
#         print("You have guessed the number, you Win.")

# modified code for better understnading of the code with rather better while condition and use of variables
import random


def checkNum(guess, n, attempts):
    if guess > n:
        print("Too high")
        return attempts - 1
    elif guess < n:
        print("Too low")
        return attempts - 1
    else:
        print("You Win !!")


playnext = "y"

while playnext == "y":

    print(logo)
    playnext = input(
        "Would you like to play the number guessing game?? Type 'y' to play and 'n' to exit : "
    )

    if playnext == "n":
        break

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 to 100.")

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard' : ")
    num = random.randint(1, 100)

    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5

    guessNum = 0
    while guessNum != num and attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guessNum = int(input("Make a guess: "))
        attempts = checkNum(guessNum, num, attempts)
        if attempts == 0:
            print(f"You have run out of guesses,the number was {num}, you Lose.")
