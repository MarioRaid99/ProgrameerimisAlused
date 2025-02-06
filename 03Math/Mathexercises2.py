"""Math exercises vol2."""

import math


def time_converter(seconds: int) -> str:
    """Convert time in seconds to hours and minutes."""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"{seconds} sekundit on {hours} tund(i) ja {minutes} minut(it)."


def student_helper(angle: int) -> str:
    """Return the sine and cosine of the given angle in degrees."""
    sine = round(math.sin(math.radians(angle)), 1)
    cosine = round(math.cos(math.radians(angle)), 1)
    return f"Nurk: {angle}, siinus: {sine}, koosinus: {cosine}."


def greetings(n: int) -> str:
    """Return a string that contains 'Hey' n times."""
    lots_of_heys = "Hey" * n
    return lots_of_heys.strip()


def adding_numbers(num_a: int, num_b: int) -> str:
    """Return given numbers concatenated together as a string."""
    return str(num_a) + str(num_b)


if __name__ == '__main__':
    assert time_converter(3661) == "3661 sekundit on 1 tund(i) ja 1 minut(it)."
    assert time_converter(7322) == "7322 sekundit on 2 tund(i) ja 2 minut(it)."

    assert student_helper(30) == "Nurk: 30, siinus: 0.5, koosinus: 0.9."

    assert greetings(3) == "HeyHeyHey"
    assert greetings(1) == "Hey"

    assert adding_numbers(2, 5) == "25"
    assert adding_numbers(3, 7) == "37"

    print("OK")
