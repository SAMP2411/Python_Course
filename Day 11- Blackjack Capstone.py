logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

import random
import os


def clearConsole():
    command = "clear"
    if os.name in ("nt", "dos"):  # If Machine is running on Windows, use cls
        command = "cls"
    os.system(command)


def addCard(sumP, anyCards):
    card = random.choice(cards)
    anyCards.append(card)
    sumP = sumP + card
    return sumP


def findFinalSum(sumComp):
    while sumComp < 17:
        sumComp = addCard(sumComp, computerCards)
    return sumComp


def findWinner(sumPlayer, sumComputer):
    while True:
        if sumPlayer == 21:
            print("You scored BlackJack. You WIN !!")
        elif sumComputer == 21:
            print("Opponent has scored BlackJack. You LOOSE !!")
        elif sumComputer > 21:
            print("Opponent went over. You WIN !!")
        elif sumPlayer > 21:
            print("You went over. You LOOSE !!")
        elif sumPlayer == sumComputer:
            print("DRAW !!")
        elif sumComputer > sumPlayer:
            print("Your score is low.You LOOSE !!")
        elif sumComputer < sumPlayer:
            print("Your score is high.You WIN !!")
        # winnerFound = True
        break

def printInfo():

    print(f"\tYour cards: {yourCards}, current score: {sumPlayer}")
    print(f"\tComputer's first card: {computerCards}")


def printFinalInfo(sumComputer, sumPlayer):
    print(f"\tYour final hand: {yourCards}, final score: {sumPlayer}")
    print(f"\tComputer's final hand: {computerCards}, final score: {sumComputer}")


def calculate(sumPlayer, sumComputer):
    while True:
        continueornot = input("Type 'y' to get anoter card, type 'n' to pass: ")
        if continueornot == "n":

            sumComputer = findFinalSum(sumComputer)

            if sumComputer > 21:
                for x in range(len(computerCards)):
                    if computerCards[x] == 11:
                        sumComputer = sumComputer - 10

            sumComputer = findFinalSum(sumComputer)

            printFinalInfo(sumComputer, sumPlayer)

            findWinner(sumPlayer, sumComputer)

        elif continueornot == "y":
            sumPlayer = addCard(sumPlayer, yourCards)
            printFinalInfo(sumComputer, sumPlayer)
            if sumPlayer >= 21:
                findWinner(sumPlayer, sumComputer)

            else:
                calculate(sumPlayer, sumComputer)
        break


def mainFn(startedornot):
    flag1 = True

    if startedornot == "y":
        print(logo)
        winnerFoud = False
        global sumPlayer, sumComputer, yourCards, computerCards
        sumPlayer = 0
        sumComputer = 0

        yourCards = []
        computerCards = []

        sumPlayer = addCard(sumPlayer, yourCards)
        sumPlayer = addCard(sumPlayer, yourCards)
        sumComputer = addCard(sumComputer, computerCards)

        printInfo()

        if sumPlayer == 21 or sumComputer == 21:

            findWinner(sumPlayer, sumComputer)
            winnerFoud = True

        if not winnerFoud:
            calculate(sumPlayer, sumComputer)


global flag
flag = True
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


while flag:
    startedornot = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ")
    clearConsole()
    mainFn(startedornot)
    if startedornot == "n":
        flag = False
