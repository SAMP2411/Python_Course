import random

# random_integer = random.randint(100, 200)
# print(random_integer)

# random_float = random.random()
# print(random_float)

# head or tail ---------------------------------------------------------------------
# rand_int = random.randint(0, 1)
# if rand_int == 1:
#     print("Heads")
# else:
# print("Tails")

# generate a random name from a string of name where names are separated by comma and space
# strName = "panchal, samarth, ved, akshil"
# split_names_list = strName.split(", ")
# l = len(split_names_list)
# print(split_names_list)
# rand_l = random.randint(0, l - 1)
# print(split_names_list[rand_l])

# put the treasure in the matrix ------------------------------------------------------------------
# row1 = ["⬜️", "⬜️", "⬜️"]
# row2 = ["⬜️", "⬜️", "⬜️"]
# row3 = ["⬜️", "⬜️", "⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# place = input("where do you want to put the treasure ?")

# p1 = place[0]
# p2 = place[1]

# first_index = int(p1) - 1
# second_index = int(p2) - 1

# map[second_index][first_index] = " X"
# print(map[0])
# print(map[1])
# print(map[2])

# rock, paper, scissor Game ------------------------------------------------------------------------

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

getImages = [rock, paper, scissor]

userMove = int(
    input("Which move do you make ? Type 0 for rock, 1 for paper, 2 for scissor\n")
)
rand = random.randint(0, 2)

if userMove > 2 or userMove < 0:
    print("Invalid Number. You Lose ")
else:
    print("\nYou have shown :\n")
    print(getImages[userMove])

    print("\nComputer has shown :\n")
    print(getImages[rand])

    if userMove == rand:
        print("Tie Game !!")
    elif userMove == 0 and rand == 2:
        print("You Win !!")
    elif userMove == 2 and rand == 0:
        print("You Lose")
    elif userMove < rand:
        print("You Lose")
    elif userMove > rand:
        print("You Win !!")

    print("\n")