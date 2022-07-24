#!/usr/bin/python3
"""Integer addition module
"""


def add_integer(a, b=98):
    """add_integer(a, b= 98)
    The function takes two arguments a, b and returns the sum.


    Args:
        a (int, float): first argument
        b (int, float): Second argument Defaults to 98.

    Returns:
        int: sum of both values
    """
    
    if type(a) is float:
        a = int(a)
    elif type(a) is not int:
        raise TypeError('a must be an integer')

    if type(b) is float:
        b = int(b)
    elif type(b) is not int:
        raise TypeError('b must be an integer')
    
    return a + b
