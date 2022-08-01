#!/usr/bin/python3
"""A python module to check if an object is an instance of a class
    """


def is_kind_of_class(obj, a_class):
    """is_kind_of_class(obj, a_class)

    Args:
        obj (any): object to check
        a_class (class): class to test obj with

    Returns: True if the object is an instance of,
    or if the object is an instance of a class that
    inherited from, the specified class ; otherwise False.
    """

    return isinstance(obj, a_class)
