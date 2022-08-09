#!/usr/bin/python3
"""
Create a Square class, inheriting from Rectangle.
"""

from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square()

    Args:
        Rectangle (class): inheritance
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Square arguments

        Args:
            size (int): Dimension/Position of the square
            x (int, optional): Dimension/Position of the square. Defaults to 0.
            y (int, optional): Dimension/Position of the square. Defaults to 0.
            id (int, optional): Dimension/Position of the square.
            Defaults to None.
        """

        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of a Square instance."""

        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.__width)

    @property
    def size(self):
        """Retrieves the size attribute."""

        return self.__width

    @size.setter
    def size(self, value):
        """Sets the size attribute."""

        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """Updates attributes of an instance."""

        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Square."""

        to_dict = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return to_dict
