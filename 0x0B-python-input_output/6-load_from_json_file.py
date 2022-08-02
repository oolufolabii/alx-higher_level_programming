#!/usr/bin/python3
"""Python module that creates an Object from a “JSON file”
    """

import json


def load_from_json_file(filename):
    """ load_from_json_file(filename)

    Args:
        filename (object): JSON file

    Returns:
        returns object file
    """

    with open(filename, 'r') as file:
        return json.load(file)
