#!/usr/bin/python3
"""a module that adds all arguments to a Python list,
and then save them to file.
"""

import sys
import os.path

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

file = 'add_item.json'

arg_list = []

if os.path.exists(file) and os.path.getsize(file) > 0:
    arg_list = load_from_json_file(file)

if len(sys.argv) > 1:
    for item in sys.argv[1:]:
        arg_list.append(item)

save_to_json_file(arg_list, file)
