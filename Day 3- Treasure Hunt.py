# leap year or not ------------------------------------------------------------
# year = 1200
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("leap year")
#         else:
#             print("not leap year")
#     else:
#         print("Leap year")
# else:
#     print("not leap year")

# love calculator----------------------------------------------------------------
# your_name = input("Your name is ?")
# her_name = input("Her name is ?")

# your_name.lower()
# her_name.lower()

# your_name = your_name + her_name

# t_count1 = your_name.count("t")
# r_count1 = your_name.count("r")
# u_count1 = your_name.count("u")
# e_count1 = your_name.count("e")
# l_count1 = your_name.count("l")
# o_count1 = your_name.count("o")
# v_count1 = your_name.count("v")

# score = ((t_count1 + r_count1 + u_count1 + e_count1) * 10) + (
#     l_count1 + o_count1 + v_count1 + e_count1
# )

# if score <= 10 and score >= 90:
#     print(f"Your score is {score}, you go togther like coke and mentos.")
# elif score >= 40 and score <= 50:
#     print(f"Your score is {score}, you are alright together.")
# else:
#     print(f"Your score is {score}")

# Treasure Island ------------------------------------------------------------------------
print("Welcome to Treasure Island!!")
print("Your mission is to find the treasure.")

choice1 = input(
    'You\'re at a crossroad, where do you want to go? Type "left" or "rigt".'
).lower()

if choice1 == "right":
    print("You fell into a hole. Game Over.")
elif choice1 == "left":
    choice2 = input(
        'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.'
    ).lower()
    if choice2 == "wait":
        choice3 = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, one blue. Which colour do you choose? "
        ).lower()
        if choice3 == "red":
            print("You found a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You win!")
        elif choice3 == "blue":
            print("You enter a room full of hungry beasts. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")