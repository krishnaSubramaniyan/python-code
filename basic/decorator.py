# decorators extends base function and without modify base function
from typing import Callable

#Without arguments
def add_sprinkles(function):
    def wrapper():
        print("sprinkles added")
        function()
    return wrapper

@add_sprinkles
def make_ice_cream():
    print(f"Here is your ice cream")

make_ice_cream()


# With arguments
def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("sprinkles added")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
def make_ice_cream(flavor):
    print(f"Here is your {flavor} Ice Cream")

make_ice_cream("venilla")