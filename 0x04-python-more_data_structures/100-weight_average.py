#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    numerator = 0
    demoninator = 0
    for item in my_list:
        numerator += (item[0] * item[1])
        demoninator += item[1]
    return numerator / demoninator
