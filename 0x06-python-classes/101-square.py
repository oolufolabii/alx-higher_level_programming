#!/usr/bin/python3

"""Square generating class for Python
"""


class Square:

    """
    A python class representing a square.
    Declared with Private Instance Attribute "size".

    Declared with Private Instance Attribute "position".

    Public instance method "area" returns
    the area of the square based on its size.
    
    Public instance method "my_print" 
    """

    def __init__(self, size=0, position=(0,0)):
        """
        Initializing the size data.
        """
        self.__size = size
        self.__position = position

    def __str__(self):
        """
        Str method to print from main module.
        """
        my_str = ""
        if self.__size == 0:
            return ''
        else:
            my_str += '\n' * self.__position[1]
            for i in range(0, self.__size):
                my_str += ' ' * self.__position[0]
                my_str += '#' * self.__size
                my_str += '\n'
            return my_str[:-1]

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

    @property
    def position(self):
        """
        Retrieving the set position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position to a value.
        """

        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")

        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates and return the current square area based on given size.
        """
        area_of_square = self.__size ** 2

        return area_of_square

    def my_print(self):
        """
        Prints in stdout the square with the character #
        """
        if self.__size == 0:
            print()
            return

        else:
            for y in range(0, self.__position[1]):
                print()
            for i in range(0, self.__size):
                for x in range(0, self.__position[0]):
                    print(" ", end="")
                for j in range(0, self.__size):
                    print("#", end="")
                print()
