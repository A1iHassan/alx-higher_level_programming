#!/usr/bin/python3
"""a module for task 4"""


def inherits_from(obj, a_class):
    """checks if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class
    """
    return isinstance(obj, a_class)
