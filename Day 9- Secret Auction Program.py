import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)


def clearConsole():
    command = "clear"
    if os.name in ("nt", "dos"):  # If Machine is running on Windows, use cls
        command = "cls"
    os.system(command)


print("Welcome to Secret Auction Program.\n")

# solving the code by list-------------------------------------------------------------------------------------
# flag = True
# name_list = []
# bid_list = []

# while flag:

#     name = input("What is your name?: ")
#     name_list.append(name)
#     bid = int(input("What's your bid?:   $"))
#     bid_list.append(bid)

#     checkAvailableBidders = input(
#         "\nAre there any other bidders?  Type 'yes' or 'no'\n"
#     )
#     clearConsole()
#     if checkAvailableBidders.lower() == "no":
#         flag = False
#         index = bid_list.index(max(bid_list))
#         print(f"The winner is {name_list[index]} with a bid of ${bid_list[index]}")

# solving the code by dict-------------------------------------------------------------------------------------
bid = {}
biddingContinue = True
highestBid = 0
winner = ""
while biddingContinue:
    name = input("What is your name?: ")
    bid[name] = int(input("What's your bid?:   $"))
    print(bid)

    checkAvailableBidders = input(
        "\nAre there any other bidders?  Type 'yes' or 'no'\n"
    )
    clearConsole()

    if checkAvailableBidders.lower() == "no":
        biddingContinue = False
        for key in bid:
            if bid[key] > highestBid:
                highestBid = bid[key]
                winner = key

        print(f"The winner is {winner} with a bid of ${bid[winner]}")
