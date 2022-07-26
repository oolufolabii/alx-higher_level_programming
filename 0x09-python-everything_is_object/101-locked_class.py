#!/usr/bin/python3
'''A module containing a restriced class.
'''


class LockedClass:
    """LockedClass
    This class is locked to only one attribute
    which is the 'first_name'
    """
    __slots__ = ['first_name']
