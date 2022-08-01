#!/usr/bin/python3
"""A python class inheriting from int
    """


class MyInt(int):
    """MyInt()
    Reverses the properties == and !=

    Args:
        int (int)
    """
    def __eq__(self, __x):
        """== becomes !=

        Args:
            __x (object)

        Returns:
            boolean 
        """
        return super().__ne__(__x)
    
    def __ne__(self, __x):
        """!= become ==

        Args:
            __x (object): 

        Returns:
            boolean 
        """
        return super().__eq__(__x)
