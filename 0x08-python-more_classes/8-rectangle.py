#!/usr/bin/python3
"""
Defines a Rectangle class.
"""


class Rectangle:
    """A rectangle class constructed by width and height
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """__init__(self, width=0, height=0)

        Args:
            width (int, optional): width of the rectangle. Defaults to 0.
            height (int, optional): height of the rectangle. Defaults to 0.
            number_of_instances(int, optional): increments the number
                of instances created, decrements with every deletion.
                Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """__str__(self)

        Returns:
                str: Returns an informal and nicely printable
                string representation of a Rectangle instance,
                filled with the '#' character.
        """
        if self.__height == 0 or self.__width == 0:
            return ''
        rec_str = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rec_str += str(self.print_symbol)
            rec_str += '\n'
        return rec_str[:-1]

    def __repr__(self):
        """__repr__(self)

        Returns:
            str: Return a string representation of a Rectangle instance
            that is able to recreate a new instance by using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """__del(self)
        Deletes a Rectangle instance.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

    def area(self):
        """area(self)

        Returns:
            area(int): returns the area of the rectangle
            based on the width and height
        """
        return self.__width * self.__height

    def perimeter(self):
        """perimeter(self)

        Returns:
            perimeter(int): returns the perimeter of the rectangle
            based on the width and height
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """bigger_or_equal(rect_1, rect_2)

        Args:
            rect_1 (int): an instance of Rectangle
            rect_2 (int): an instance of Rectangle

        Raises:
            TypeError: must be an instance of Rectangle
            TypeError: must be an instance of Rectangle

        Returns:
            int|Rectangle obect: returns the biggest
                rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2
