# n = 55
# sum = int(n / 10) + n % 10
# print(sum)
# age = 19
# print(
#     "You have "
#     + str(((90 - age) * 365))
#     + " days, "
#     + str(((90 - age) * 52))
#     + " and "
#     + str(((90 - age) * 12))
#     + " months left!!"
# )
print("Welcome to the tip calculator")
total_bill = int(input("What is your total bill? $"))
perc_tip = int(input("What percentage tip would you like to give ? 10, 12 or 15?"))
n_people = int(input("How many people to split the bill?"))
new_total = total_bill + total_bill * (perc_tip / 100)
split_amount = round(new_total / n_people, 2)
print(f"Each person should pay : $ {split_amount}")