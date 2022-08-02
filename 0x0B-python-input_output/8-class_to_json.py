#!/usr/bin/python3
"""a python function that returns the dictionary description
with simple data structure for JSON serialization of
an object
    """


def class_to_json(obj):
    """class_to_json(obj)

    Args:
        obj: object to convert

    Returns: dictionary description of obj
    """

    return obj.__dict__
