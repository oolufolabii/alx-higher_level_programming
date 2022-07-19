#!/usr/bin/python3
class Square:

    """
    A python class representing a square.
    Declared with Private Instance Attribute "size".
    """

    def __init__(self, size=0):
        """
        Initializing the size data.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
