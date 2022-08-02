#!/usr/bin/python3
"""A python function that inserts a line of text to a file,
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """append_after(filename, search_string, new_string)

    Args:
        filename: name of the file
        search_string: string to append after
        new_string: new_string to append
    """

    with open(filename, "r") as file:
        text = file.read()

    with open(filename, "w") as file_w:
        text = ""
        for line in text:
            text += line
            if search_string in line:
                text += new_string
        file_w.write(text)
