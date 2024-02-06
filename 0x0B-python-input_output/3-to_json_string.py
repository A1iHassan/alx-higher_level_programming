#!/usr/bin/python3
"""a module for task 3

Write a function that returns the
JSON representation of an object (string)
"""


import json


def to_json_string(my_obj):
    """Write a function that returns the
    JSON representation of an object (string)

    Args:
        my_obj: objet to be serialized

    Return:
        JSON representation
    """
    return json.dumps(my_obj)
