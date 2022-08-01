#!/usr/bin/python3
"""_summary_
"""

def is_same_class(obj, a_class):
    """_summary_

    Args:
        obj (class instance): obj to test
        a_class (class): class to test against
        
    Return: True is obj is an instance of a_class, False if otherwise
    """
    
    return (type(obj) == a_class)
