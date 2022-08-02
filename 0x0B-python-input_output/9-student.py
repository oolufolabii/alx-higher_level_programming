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

    def to_json(self):
        """returns a dictionary format of the student instance

        """

        return self.__dict__
