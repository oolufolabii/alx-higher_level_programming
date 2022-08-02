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

    with open(filename, 'r+', encoding='utf-8') as new_file:
        lines = new_file.readlines()
        new_file.seek(0)
        for i, line in enumerate(lines):
            #            print("read:   {}".format(line), end='')
            if search_string in line:
                lines[i] = line + new_string
                #                print("modded: {}".format(line), end='')
    #        for line in lines:
    #            print(line, end="")
        new_file.writelines(lines)
