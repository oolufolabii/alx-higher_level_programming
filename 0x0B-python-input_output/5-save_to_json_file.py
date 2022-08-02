#!/usr/bin/python3

import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file(my_obj, filename)

    Args:
        my_obj (JSON): JSON object to write
        filename (file): file to write into
    """

    with open(filename, 'w') as file:
        json.dump(my_obj, file)
