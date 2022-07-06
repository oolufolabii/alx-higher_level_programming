#!/usr/bin/python3
def search_replace(my_list, search, replace):
    replacement_list = []
    for item in my_list:
        if item == search:
            replacement_list.append(replace)
        else:
            replacement_list.append(item)
    return replacement_list

my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)