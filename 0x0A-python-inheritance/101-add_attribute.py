#!/usr/bin/python3
"""Python module to check if attributes
can be added to an object
"""


def add_attribute(obj, attrib, value):
    """add_attribute(obj, attrib, value):

    Args:
        obj: object to add the attribute to
        attrib: name of the attribute
        value: value of the attribute to add
    """

    if not hasattr(obj, '__slots__') and not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    if hasattr(obj, '__slots__') and not hasattr(obj, attrib):
        raise TypeError("can't add new attribute")

    setattr(obj, attrib, value)
