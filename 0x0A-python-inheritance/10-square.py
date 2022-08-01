#!/usr/bin/python3
"""A python class for a square
    """

BaseGeometry = __import__('7-base_geometry.py').BaseGeometry
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """Square()

    Args:
        Rectangle (class): inheriting the rectangle class
    """

    def __init__(self, size):
        """Square(size)

        Args:
            size (int): the size of the sides of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

        def __str__(self):
            return super().__str__()

        def area(self):
            """area() returns the area of the square
            """
            return self.__size ** 2
