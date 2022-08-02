#!/usr/bin/python3
"""A student class
    """


class Student:
    """A class defining a student
    """

    def __init__(self, first_name, last_name, age):
        """Initialize the student instance

        Args:
            first_name (string): Student first name
            last_name (string): Student last name
            age (int): Student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dictionary format of the student instance

        Args:
            - attrs: list of attributes
        """

        my_dict = dict()
        if type(attrs) is list and all(type(item) is str for item in attrs):
            for item in attrs:
                if item in self.__dict__:
                    my_dict.update({item: self.__dict__[item]})
            return my_dict
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """reload_from_json(json)

        Args:
            json: dictionnary of attributes
        """

        for item in json:
            self.__dict__.update({item: json[item]})
