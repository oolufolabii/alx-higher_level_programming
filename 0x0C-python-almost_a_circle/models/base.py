#!/usr/bin/python3
"""Python class defined for a Base
    """

import json
import csv
import os


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

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file(cls, list_objs)


        Args:
            list_objs (list): a list of instances

        Raises:
            TypeError: must be a list of instances
        """
        if list_objs is None:
            list_objs = []

        list_dicts = []
        for item in list_objs:
            list_dicts.append(item.to_dictionary())
        json_dict = cls.to_json_string(list_dicts)

        filename = cls.__name__ + '.json'
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(json_dict)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string.

        Args:
            - json_string: string to convert to list
        """

        string_list = []
        if json_string is not None and json_string != '':
            if type(json_string) != str:
                raise TypeError("json_string must be a string")
            string_list = json.loads(json_string)
        return string_list

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.

        Args:
            - dictionary: used as **kwargs

        Returns: instance created
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""

        file_name = cls.__name__ + ".json"
        string_list = []
        list_dicts = []
        if os.path.exists(file_name):
            with open(file_name, 'r') as file:
                s = file.read()
                list_dicts = cls.from_json_string(s)
                for d in list_dicts:
                    string_list.append(cls.create(**d))
        return string_list

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes CSV format from a file.

        Returns: list of instances
        """

        filename = cls.__name__ + ".csv"
        string_list = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                reader = csv.reader(f, delimiter=',')
                if cls.__name__ == 'Rectangle':
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    fields = ['id', 'size', 'x', 'y']
                for x, row in enumerate(reader):
                    if x > 0:
                        i = cls(1, 1)
                        for j, e in enumerate(row):
                            if e:
                                setattr(i, fields[j], int(e))
                        string_list.append(i)
        return string_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a Turtle window and draws
        rectangles and squares.

        Args:
            - list_rectangles: list of Rectangle instances
            - list_squares: list of Square instances
        """

        import turtle
        import time
        from random import randrange

        t = turtle.Turtle()
        t.color("beige")
        turtle.bgcolor("violet")
        t.shape("square")
        t.pensize(8)

        for i in (list_rectangles + list_squares):
            t.penup()
            t.setpos(0, 0)
            turtle.Screen().colormode(255)
            t.pencolor((randrange(255), randrange(255), randrange(255)))
            Base.draw_rect(t, i)
            time.sleep(1)
        time.sleep(5)

    @staticmethod
    def draw_rect(t, rect):
        """Helper method that draws a Rectangle
        or Square.
        """

        t.penup()
        t.setpos(rect.x, rect.y)
        t.pendown()
        t.forward(rect.width)
        t.left(90)
        t.forward(rect.height)
        t.left(90)
        t.forward(rect.width)
        t.left(90)
        t.forward(rect.height)
