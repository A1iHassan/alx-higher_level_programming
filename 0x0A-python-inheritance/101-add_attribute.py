#!/usr/bin/python3
"""a module for task 13

a function that adds a new attribute to
an object if it's possible
"""


def add_attribute(obj, name, atr):
    """a function that adds a new attribute to
    an object if it's possible

    Args:
        obj: object to add to
        name: attribute key
        atr: attribute value
    """

    if hasattr(obj, '__dict__') or hasattr(type(obj), '__dict__'):
        setattr(obj, name, atr)
    else:
        raise TypeError("can't add new attribute")
