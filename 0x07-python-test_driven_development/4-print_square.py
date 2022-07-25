#!/usr/bin/python3
"""
Python Module print_square
Prints a square with the character #.
"""


def print_square(size):
    """print_square(size)

    Args:
        size (int):  is the size length of the square

    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for num_1 in range(size):
        for num_2 in range(size):
            print('#', end='')
        print()
