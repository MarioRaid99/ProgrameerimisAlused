"""Tuple exercises."""

def get_sum_and_diff(a: int, b: int) -> tuple:
    """
    Return sum of a and b and diff of a and b.
    """
    return a + b, a - b


def create_tuple_from_two_numbers(a: int, b: int) -> tuple:
    """
    Create a tuple with either one or two elements based on equality.
    """
    return (a,) if a == b else (a, b)


def create_tuple_up_to_n(n: int) -> tuple:
    """
    Create tuple with numbers from 0 to n, inclusive.
    """
    return tuple(range(n + 1)) if n >= 0 else ()


def merge_tuples(a: tuple, b: tuple) -> tuple:
    """
    Merge two tuples.
    """
    return a + b


def remove_odd_numbers(numbers: tuple) -> tuple:
    """
    Remove odd numbers from a tuple.
    """
    return tuple(num for num in numbers if num % 2 == 0)


def insert_tuple_inside_tuple(outer_tuple: tuple, position: int, inner_tuple: tuple) -> tuple:
    """
    Insert inner_tuple inside outer_tuple at a given position.
    """
    return outer_tuple[:position] + inner_tuple + outer_tuple[position:]

if __name__ == '__main__':
    print(get_sum_and_diff(4, 5))
    print(create_tuple_from_two_numbers(4, 5))
    print(create_tuple_up_to_n(5))
    print(merge_tuples(4, 5))
    print(remove_odd_numbers((4, 5)))
    print(insert_tuple_inside_tuple(outer_tuple=(), position=0, inner_tuple=()))