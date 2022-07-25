#!/usr/bin/python3
"""
Defines a Rectangle class.
"""


class Rectangle:
    """A rectangle class constructed by width and height
    """

    def __init__(self, width=0, height=0):
        """__init__(self, width=0, height=0)

        Args:
            width (int, optional): width of the rectangle. Defaults to 0.
            height (int, optional): height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width(self)

        Returns:
            __width: Retrieves the width of a Rectangle instance.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width(self, value)

        Args:
            value (int): sets the width of the rectangle

        Raises:
            TypeError: width must be an integer
            ValueError: width must be greater than zero
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height(self)

        Returns:
            __height: Retrieves the height of a Rectangle instance.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height(self, value)

        Args:
            value (int): sets the height of the rectangle

        Raises:
            TypeError: height must be an integer
            ValueError: height must be greater than zero
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
