# Password Generator Project
import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# my way of solving the code--------------------------------------------------------------------------
# password = ""
#
# for i in range(0, nr_letters):
#     randL = random.randint(0, nr_letters - 1)
#     password = password + letters[randL]

# for i in range(0, nr_symbols):
#     randS = random.randint(0, nr_symbols - 1)
#     password = password + numbers[randS]

# for i in range(0, nr_numbers):
#     randN = random.randint(0, nr_numbers - 1)
#     password = password + symbols[randN]

# print(password)


# the course's way of solving the code------------------------------------------------------------------
password_list = []

for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = ""
for i in password_list:
    password += i
print(password)