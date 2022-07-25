#!/usr/bin/python3
"""
Python Module: say_my_name
Prints a first name and last name.
"""


def say_my_name(first_name, last_name=""):
    """say_my_name(first_name, last_name="")

    Args:
        first_name (str): must be strings
        last_name (str, optional): must be strings. Defaults to "".

    Raises:
        TypeError: first_name must be a string or
        last_name must be a string
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
