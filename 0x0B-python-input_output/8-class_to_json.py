#!/usr/bin/python3
"""a module for task 8

a function that returns the dictionary description
with simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""


def class_to_json(obj):
    """Returns a dictionary description of
    the object suitable for JSON serialization.

    Args:
        obj: An instance of a class.

    Returns:
        A dictionary containing serializable attributes of the object.
    """
    obj_dict = obj.__dict__

    for key, value in obj_dict.items():
        if isinstance(value, (list, dict, str, int, bool)):
            continue
        elif isinstance(value, (tuple, set)):
            obj_dict[key] = list(value)
        elif hasattr(value, '__dict__'):
            obj_dict[key] = class_to_json(value)

    return obj_dict
