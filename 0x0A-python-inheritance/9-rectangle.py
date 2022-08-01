#!/usr/bin/python3
"""Python class module for a rectangle"
    """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class

    Summary:
        BaseGeometry (class): inheriting from the BaseGeometry class
    Args:
        -width: width property of the rectangle
        -height: height property of the rectangle
    """

    def __init__(self, width, height):
        """Rectangle(width, height)

        Args:
        -width: width property of the rectangle
        -height: height property of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Return a formatted string
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """area(self)

        Returns:
            area(int): returns the area of a rectangle
        """

        return self.__width * self.__height
