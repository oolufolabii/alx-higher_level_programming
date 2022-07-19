#!/usr/bin/python3
"""Square generating class for Python
"""


class Square:

    """
    A python class representing a square.
    Declared with Private Instance Attribute "size".

    Public instance method "area" returns
    the area of the square based on its size.
    """

    def __init__(self, size=0):
        """
        Initializing the size data.
        """
        self.__size = size

    def __eq__(self, other):
        """Equal."""
        if hasattr(other, 'size'):
            return self.__size == other.__size
        return self.__size == other

    def __ne__(self, other):
        """Not equal."""
        return not self.__eq__(other)

    def __lt__(self, other):
        """Less than."""
        if hasattr(other, 'size'):
            return self.__size < other.__size
        return self.__size < other

    def __le__(self, other):
        """Less than or equal."""
        if hasattr(other, 'size'):
            return self.__size <= other.__size
        return self.__size <= other

    @property
    def size(self):
        """
        Retrieving the size value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setting a value and type to size. Raising exceptions otherwise.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and return the current square area based on given size.
        """
        area_of_square = self.__size ** 2

        return area_of_square
