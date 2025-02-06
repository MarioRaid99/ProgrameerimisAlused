"""Function examples."""


def func() -> None:
    """Print a message to indicate the function is called."""
    print("I´m inside the function")


def my_name_is(name: str) -> None:
    """Print the user's name to the console.

    :param name: The name to print.
    """
    print(f"My name is {name}")


def sum_six(num: int) -> int:
    """Return the sum of six and the given number.

    :param num: The number to add to six.
    :return: The sum of six and the given number.
    """
    return 6 + num


def sum_numbers(num1: int, num2: int) -> int:
    """Return the sum of two numbers.

    :param num1: The first number.
    :param num2: The second number.
    :return: The sum of num1 and num2.
    """
    return num1 + num2


def usd_to_eur(usd_a: int) -> float:
    """Convert USD to EUR using a fixed exchange rate.

    :param usd_a: The amount in USD.
    :return: The equivalent amount in EUR.
    """
    return usd_a * 0.8


if __name__ == "__main__":
    func()
    my_name_is("Mario")
    my_name_is("Mairo")
    print(sum_six(6))
    print(sum_numbers(8, 5))
    print(usd_to_eur(100))
