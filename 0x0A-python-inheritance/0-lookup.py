#!/usr/bin/python3
"""A python module on printing available
class attributes and methods.
"""

def lookup(obj):
    """lookup(obj)

    Args:
        obj (instance): returns list of attributes and methods
    """
    
    return dir(obj)
