"""Math exercises."""
import math


def sum_and_difference(num_a: int, num_b: int) -> tuple:
    """Return the sum and difference of given variables num_a and num_b."""
    sum_ = num_a + num_b
    difference = num_a - num_b
    return sum_, difference


def float_division(num_a: int, num_b: int) -> float:
    """Divide given variables num_a and num_b and return the result."""
    division = num_a / num_b
    return division


def integer_division(num_a: int, num_b: int) -> int:
    """Divide given variables num_a and num_b and return the result rounded down."""
    division = num_a // num_b
    return division


def powerful_operations(num_a: int, num_b: int) -> tuple:
    """Return the product of given variables, num_a to the power of num_b and the remainder of division of variables."""
    multiply_numbers = num_a * num_b
    power = num_a ** num_b
    remainder = num_a % num_b
    return multiply_numbers, power, remainder


def find_average(num_a: int, num_b: int) -> float:
    """Return the average of given variables."""
    average = (num_a + num_b) / 2
    return average


def area_of_a_circle(radius: float) -> float:
    """Calculate and return the area of a circle."""
    return round(math.pi * radius ** 2, 2)


def area_of_an_equilateral_triangle(side_length: float) -> int:
    """Calculate and return the area of an equilateral triangle."""
    return int(round((math.sqrt(3) / 4) * side_length ** 2, 0))


def calculate_discriminant(a: int, b: int, c: int) -> int:
    """Calculate discriminant with given variables and return the result."""
    discriminant = b ** 2 - 4 * a * c
    return discriminant


def calculate_hypotenuse_length(a: int, b: int) -> float:
    """Return the length of hypotenuse when the lengths of the catheti are given."""
    c = math.sqrt(a ** 2 + b ** 2)
    return c


def calculate_cathetus_length(a: int, c: int) -> float:
    """Return the length of cathetus when the lengths of the second cathetus and hypotenuse are given."""
    return math.sqrt(c ** 2 - a ** 2)


if __name__ == '__main__':
    assert sum_and_difference(5, 6) == (11, -1)
    assert sum_and_difference(11, 9) == (20, 2)

    assert float_division(9, 3) == 3.0
    assert round(float_division(10, 3), 2) == 3.33

    assert integer_division(10, 3) == 3
    assert integer_division(7, 10) == 0

    assert powerful_operations(10, 3) == (30, 1000, 1)
    assert powerful_operations(2, 10) == (20, 1024, 2)

    assert find_average(8, 5) == 6.5
    assert find_average(999, 999) == 999

    assert round(area_of_a_circle(7), 2) == 153.94
    assert area_of_a_circle(19) == 1134.11

    assert area_of_an_equilateral_triangle(5) == 11
    assert area_of_an_equilateral_triangle(15) == 97

    assert calculate_discriminant(3, 10, 5) == 40
    assert calculate_discriminant(2, 8, 6) == 16

    assert calculate_hypotenuse_length(5, 7) == 8.602325267042627
    assert calculate_hypotenuse_length(3, 10) == 10.44030650891055

    assert calculate_cathetus_length(10, 19) == 16.15549442140351
    assert calculate_cathetus_length(4, 5) == 3.00

    print("OK")