#!/usr/bin/python3
"""Python module to append string to the end of a file
    """


def append_write(filename="", text=""):
    """append_write(filename, text)

    Args:
        filename (str, optional): Name of the file, with its extension.
        Defaults to "".
        text (str, optional): String to write to the file. Defaults to "".

    Returns:
        filename: returns the file with the text content appended to the end.
    """

    with open(filename, mode="a") as file:
        return file.write(text)
