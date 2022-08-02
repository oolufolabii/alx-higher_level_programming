#!/usr/bin/python3
"""Reads from filename and prints its contents to stdout.
    """


def read_file(filename=""):
    """read_file(filename)

    Args:
        filename (str, optional): The filename to read and stdout.
        Defaults to "".
    """
    with open(filename, encoding="utf-8") as file:
        data = file.read()
        print(data)
