#!/usr/bin/python3
"""
Python Module text_indentation
Adds two new lines after a set of characters.
"""


def text_indentation(text):
    """text_indentation(text)

    Args:
        text (str): text must be a string

    Raises:
        TypeError: Raise an exception where text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delimiter = ".:?"
    for char in delimiter:
        text = (char + "\n\n").join(
            [line.strip(" ") for line in text.split(char)])

    print("{}".format(text), end="")
