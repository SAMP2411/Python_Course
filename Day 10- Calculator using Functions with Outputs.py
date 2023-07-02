# # Convert a name given by user into title case
# def format_name(f, l):
#     """ This is a function to convert first name and last name into title case"""
#     ff = f[:1]
#     ff = ff.upper()
#     lf = l[:1]
#     lf = lf.upper()
#     fl = f[1:]
#     fl = fl.lower()
#     ll = l[1:]
#     ll = ll.lower()

#     return ff + fl + " " + lf + ll


# while True:
#     firstName = input("Enter first name : ")
#     lastName = input("Enter last name : ")

#     print("Correct name is : " + format_name(firstName, lastName))

# # Calculator using functions with outputs
# flag = True


# def calculate(operator, num1, num2):
#     if operator == "/":
#         ans = num1 / num2
#     elif operator == "*":
#         ans = num1 * num2
#     elif operator == "-":
#         ans = num1 - num2
#     elif operator == "+":
#         ans = num1 + num2
#     else:
#         print("Invalid Opeartor !!")

#     return ans


# while flag:
#     num1 = int(input("What's the first number?: "))
#     operation = input("Pick an operation [ + - * / ]: ")
#     num2 = int(input("What's the next number?: "))

#     print(f"{num1} {operation} {num2} = {calculate(operation,num1,num2)} ")

# # Calculator in the way its created in the course
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": sub, "*": multiply, "/": divide}


def calculate():
    print(logo)
    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    flag = "y"

    while flag == "y":
        operation = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        answer = operations[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {answer} ")
        if (
            input(
                f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: "
            )
            == "y"
        ):
            num1 = answer
        else:
            flag = False
            calculate()


calculate()