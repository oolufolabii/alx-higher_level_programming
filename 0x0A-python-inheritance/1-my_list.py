#!/usr/bin/python3
"""A module inheriting from the list class

"""

class MyList(list):
    """MyList(list)

    Args:
        list (python class): python class inherited into MyList
    """
    
    def print_sorted(self):
        """print a list of sorted integers
        """
        
        sorted_list = self[:]
        sorted_list.sort()
        print(sorted_list)
