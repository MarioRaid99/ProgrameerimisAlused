import math

import pytest


def solve_quadratic_equation(a, b, c):

    disc = b**2 - 4 * a * c
    x1 = (-b - math.sqrt(disc)) / (2 * a)
    x2 = (-b + math.sqrt(disc)) / (2 * a)
    return x1, x2


def test_solve_quadratic_equation_two_float_solutions():
    x1, x2 = solve_quadratic_equation(2, 3, -57)
    assert (round(x1, 3), round(x2, 3)) == (-6.141, 4.641)

def test_solve_quadratic_equation_one_float_solutions():
    x1, x2 = solve_quadratic_equation(1, -2, 1)
    assert (round(x1, 3), round(x2, 3)) == (1.000, 1.000)

def test_solve_quadratic_equation_no_solution():
    with pytest.raises(ZeroDivisionError) as e_info:
        solve_quadratic_equation(1, -3, 1)
        assert str(e_info.value) == "float division by zero"
        assert e_info.tb.tb_lineno == 37

def test_solve_quadratic_equation_zero_solution():
    ...