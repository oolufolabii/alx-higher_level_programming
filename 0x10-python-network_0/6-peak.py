#!/usr/bin/python3
""" function to find peak value in a list """


from audioop import reverse


def find_peak(list_of_integers):
    """find_peak(list_of_integers)

    Args:
        list_of_integers (list): contains a list of integers and can be empty.
    """
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
