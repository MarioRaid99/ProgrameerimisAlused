"""Basic function exercises."""
import math


def print_hello():
    """Print "Hello"."""
    print("Hello")


def get_hello() -> str:
    """Return "Hello"."""
    return "Hello"


def ask_name_and_greet_user():
    """
    Ask for the user's name and greet them.

    If the name is "Thanos" (any capitalization), show a special message.
    Otherwise, greet the user and offer them a hamburger.
    """
    # Ask for the user's name
    name = input("What is your name? ")

    # Check if the name is Thanos (ignoring case)
    if name == "thanos":
        print("Get out of here, Thanos! Nobody wants to play with you!")
    else:
        # Capitalize the first letter of the name
        formatted_name = name.capitalize()
        print(f"Hi, {formatted_name}. Would you like to have a Hamburger?")


def calculate_hypotenuse_length(a: float, b: float) -> float:
    """Return hypotenuse value."""
    c = math.sqrt(a ** 2 + b ** 2)
    return c


def calculate_cathetus_length(a: float, c: float) -> float:
    """Return cathetus value."""
    return math.sqrt(c ** 2 - a ** 2)


if __name__ == '__main__':
    print_hello()  # should print "Hello"
    hello = get_hello()  # should return "Hello"
    print(hello)  # let's check the value of hello variable
    ask_name_and_greet_user()  # should ask name and greet
    print(calculate_hypotenuse_length(3, 4))  # should print 5.0
    print(calculate_cathetus_length(3, 5))  # should print 4.0
