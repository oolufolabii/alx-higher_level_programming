#!/usr/bin/python3
"""Magic class from a ByteCode."""
import math


class MagicClass:
    """Initializing the MagicClass."""
    def __init__(self, radius=0):
        """Initialization of the data."""
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """Calculate and return the area."""
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """Calculate and return the circumference."""
        return 2 * math.pi * self._MagicClass__radius
