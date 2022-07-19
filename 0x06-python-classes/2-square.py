#!/usr/bin/python3
"""Square generating class for Python
"""


class Square:

    """
    A python class representing an empty square.
    Declared with Instantiation with size (no type/value verification).
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
