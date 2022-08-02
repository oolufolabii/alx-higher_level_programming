#!/usr/bin/python3
"""a module that adds all arguments to a Python list,
    and then save them to a file.
    """

import sys
import json
import os.path

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

file = 'add_item.json'

argv_list = sys.argv[1:]

try:
    content = load_from_json_file(file)
except:
    content = []
finally:
    for arg in argv_list:
        content.append(arg)
    save_to_json_file(content, "add_item.json")
