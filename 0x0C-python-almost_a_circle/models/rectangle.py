#!/usr/bin/python3
"""A python package inheriting from another package
    """


from models.base import Base


class Rectangle(Base):
    """Rectangle(id=)

    Args:
        Base (Class): inheriting from Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle()

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int, optional): x position of the rectangle. Defaults to 0.
            y (int, optional): y position of the rectangle. Defaults to 0.
            id (int, optional): class id of the rectangle. Defaults to None.
        """
        super().__init__(id)

        self.width = width
        self.height = height

        self.x = x
        self.y = y

    def __validator(self, name, value):
        """self.__validator(name, value)

        Args:
            name (str): name of the value to check
            value (int): value to be validated

        Returns:
            int: validated value
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if name is "width" or name is "height":
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))

        elif name is "x" or name is "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        """__width getter

        returns __width(int): a dimension of the rectangle
        """

        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width attribute

        """
        self.__validator('width', value)

        self.__width = value

    @property
    def height(self):
        """Height getter
        """

        return self.__height

    @height.setter
    def height(self, value):
        """height setter


        """
        self.__validator('height', value)

        self.__height = value

    @property
    def x(self):
        """x position getter
        """

        return self.__x

    @x.setter
    def x(self, value):
        """x position setter


        """

        self.__validator('x', value)
        self.__x = value

    @property
    def y(self):
        """y position getter
        """

        return self.__y

    @y.setter
    def y(self, value):
        """y position setter


        """

        self.__validator('y', value)

        self.__y = value

    def area(self):
        """Rectangle.area()

        Returns:
            int: returns the area of the rectangle
        """

        return self.width * self.height

    def display(self):
        """Represents the Rectangle instance with the # character.
        """

        display = ""
        for row in range(self.y):
            display += "\n"
        for row in range(self.height):
            for column in range(self.x):
                display += " "
            for column in range(self.width):
                display += "#"
            if row < self.height - 1:
                display += "\n"
        self.__display = display

        print(display)

    def __str__(self):
        """Return a string representation for the instance
        """

        string_out = "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
        return string_out

    def update(self, *args, **kwargs):
        """Updates the attributes for an instance

        Raises:
            KeyError: for keyword arguments
            TypeError: for argument not an integer
        """
        if len(args) == 0:
            if len(kwargs) == 0 or len(kwargs) > 5:
                raise TypeError(
                    "Rectangle takes between 1 to 5 keyword"
                    "or non-keyword arguments")

            else:
                for key, value in kwargs.items():
                    if key == "id":
                        if type(value) != int and value is not None:
                            raise TypeError("id must be an integer")
                        self.id = value
                    elif key == 'width':
                        self.width = value
                    elif key == 'height':
                        self.height = value
                    elif key == 'x':
                        self.x = value
                    elif key == 'y':
                        self.y = value
                    else:
                        raise KeyError('invalid attribute name: ' +
                                       '{}'.format(key))

        elif len(args) > 5:
            raise TypeError(
                "Rectangle takes between 1 to 5 keyword or"
                "non-keyword arguments")

        else:
            for i, arg in enumerate(args):
                if i == 0:
                    if self.id != arg:
                        self.id = arg

                    elif i == 1:
                        self.width = arg

                    elif i == 2:
                        self.height = arg

                    elif i == 3:
                        self.x = arg

                    elif i == 4:
                        self.y = arg

    def to_dictionary(self):
        """to_dictionary(self):

        Returns:
            dict: returns a dictiionary representation
            of the rectangle arguments.
        """

        to_dict = {'id': self.id, 'width': self.__width,
                   'height': self.__height, 'x': self.__x, 'y': self.__y}
        return to_dict
