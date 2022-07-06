#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        temp_dict = a_dictionary.items()
        sort = (sorted(temp_dict, key=lambda item: item[1], reverse=True))
        return sort[0][0]
