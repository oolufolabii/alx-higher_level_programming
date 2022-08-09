#!/usr/bin/python3
"""Python class defined for a Base
    """


class Base:
    """Python class, with private attribute
    __nb_objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Base(id=)

        Args:
            id (int, optional): ID number for serialiaztion. Defaults to None.

        Raises:
            TypeError: if id is not an integer, raises error
        """
        if type(id) != int and id is not None:
            raise TypeError("id must be an integer")
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

        # else:
        #     Base.__nb_objects += 1
        #     self.id = Base.__nb_objects


b1 = Base()
print(b1.id)

b2 = Base()
print(b2.id)

b3 = Base()
print(b3.id)

b4 = Base(12)
print(b4.id)

b5 = Base()
print(b5.id)
