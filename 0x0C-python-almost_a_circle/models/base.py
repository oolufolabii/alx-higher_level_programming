#!/usr/bin/python3
"""Python class defined for a Base
    """

import json
from os import stat


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string(list_dictionaries)

        Args:
            list_dictionaries (list): a list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"

        if (type(list_dictionaries) != list or
           not all(type(item) == dict for item in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")

        return json.dumps(list_dictionaries)
