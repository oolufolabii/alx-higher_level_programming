#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    if len(my_list) == 0:
        return None
    [new_list.append(my_list[num] % 2 == 0) for num in range(len(my_list)-1)]
    return new_list
