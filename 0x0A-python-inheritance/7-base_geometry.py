#!/usr/bin/python3
"""A python module for base geometry"""


class BaseGeometry:
    """BaseGeometry class
    """
    def area(self):
        """area(self): Raise a 'non implemented' exception
        """

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """integer_validator(self, name, value):

        Args:
            name (string): A string
            value (int): a positive integer
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
