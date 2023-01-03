#!/usr/bin/python3
"""A module for `print_square` function."""


def print_square(size):
    """Prints a square where size is
    the length and width of the square.

    Parameters:
        size (int): the size of the square

    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
