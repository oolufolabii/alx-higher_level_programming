#!/usr/bin/python3
"""Python Module to write to a file
    """


def write_file(filename="", text=""):
    """write_file(filename, text)

    Args:
        filename (str, optional): Name of the file, with its extension. Defaults to "".
        text (str, optional): String to write to the file. Defaults to "".
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
