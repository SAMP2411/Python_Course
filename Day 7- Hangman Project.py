import random
import os


def clearConsole():
    command = "clear"
    if os.name in ("nt", "dos"):  # If Machine is running on Windows, use cls
        command = "cls"
    os.system(command)


stages = [
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
]

logo = """ 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    """


def print_list(list_l):
    out = ""
    for i in list_l:
        out += i
    return out


# hangman game-----------------------------------------------------------------------------------------------------

words_list = [
    "devarsh",
    "dharm",
    "samarth",
    "jyoti",
    "jitu",
    "yukti",
    "meena",
    "kamlesh",
]

# rand = random.randint(0, (len(words_list) - 1))
lives = 5

# name = words_list[rand].lower()
name = random.choice(words_list)
word_l = len(name)
# print(word_l)

# blank = ""
blank_list = []

for i in range(word_l):
    blank_list.append("_ ")
    # blank += "-"

# print(f"Blank is : {''.join(blank_list)}")
# print(blank)
# print("Blank list is :")
# print(blank_list)

flag = False

while lives > 0:

    a = input("Enter any alphabet : ")
    clearConsole()
    for i in range(word_l):
        if a == name[i]:
            flag = True
            break
        else:
            flag = False

    if flag:
        for i in range(word_l):
            if a == name[i]:
                blank_list[i] = a

        print(f"\nThe word is : {''.join(blank_list)}")
        # curr_blank = print_list(blank_list)
        # print(curr_blank)

    else:
        lives -= 1
        print(f"\nThe word is : {''.join(blank_list)}")
        # curr_blank = print_list(blank_list)
        # print(curr_blank)
        print(f"\nYou lost one life. Only {(lives+1)} left !!")

    print(stages[lives])

    if print_list(blank_list) == name:
        print("You Won !!")
        break

if lives == 0:
    print("You Lose !!")