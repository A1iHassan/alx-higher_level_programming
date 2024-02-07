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
    def __exit__(exc_type, exc_value, traceback):
        """determines the action when exiting
        a context manager block
        """
        if exc_type:
            raise TypeError("can't add new attribute")

    obj.__exit__ = __exit__

    with obj as obj:
        obj_dict = obj.__dict__
        obj_dict[name] = atr
