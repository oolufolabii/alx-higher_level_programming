#!/usr/bin/python3
def search_replace(my_list, search, replace):
    replacement_list = []
    for item in my_list:
        if item == search:
            replacement_list.append(replace)
        else:
            replacement_list.append(item)
    return replacement_list
