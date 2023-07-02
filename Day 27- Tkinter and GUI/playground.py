# Using *args we can have a unlimited data stored in the form of a tuple which can be accessed inside your function
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(f"Sum : {add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}")


# Using **kwargs (Key Word Arguments) we can have an unlimited data stored in the form of a dictionary which can be accessed inside your function
# You can give unlimited positional arguments which are stored as dictionary where the positional part is the key and its value is value
def calculate(n, **kwargs):
    print(kwargs)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


# Using kwargs in class
class Car:
    def __init__(self, **kw):
        # if you use below method and any argument is not specified it will show error
        # self.make = kw["make"]
        # self.model = kw["model"]

        # if you use get method if there is no value for any positional argument it will return none
        self.make = kw.get("make")
        self.model = kw.get("model")


# my_car = Car(make="Nissan", model="GT-R")
my_car = Car(make="Nissan")
print(my_car.model)
