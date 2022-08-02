#!/usr/bin/python3
"""Python module to returns the JSON format of an object.
    """
import json


def to_json_string(my_obj):
    """to_json_string(my_obj)

    Args:
        my_obj (object): a string

    Returns:
        mj_obj: returns the JSON format of my_obj
    """

    return json.dumps(my_obj)
