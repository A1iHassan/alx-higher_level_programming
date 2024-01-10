#!/usr/bin/python3
"""a module for lookup(obj) function
"""


def lookup(obj):
    """a function that returns the list of available \
        attributes and methods of an object

    Args:
        obj: wanted object
    
    Return:
        list of obj's attributes
    """
    return dir(obj)
