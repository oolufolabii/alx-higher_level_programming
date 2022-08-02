#!/usr/bin/python3
"""Python module to returns the JSON string format of an object.
    """

import json


def from_json_string(my_str):
    """from_json_string(my_str)

    Args:
        my_str (json object): JSON object

    Returns:
        my_str: returns the JSON string format
    """

    return json.loads(my_str)
