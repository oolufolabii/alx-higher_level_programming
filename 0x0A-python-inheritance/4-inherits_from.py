#!/usr/bin/python3
"""_summary_
    """


def inherits_from(obj, a_class):
    """inherits_from(obj, a_class)

    Args:
        obj (any)
        a_class (class)
        
    Return: True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.
    """
    
    return isinstance(obj, a_class) and type(obj) != a_class
