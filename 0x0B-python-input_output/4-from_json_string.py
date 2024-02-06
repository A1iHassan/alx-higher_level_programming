#!/usr/bin/python3
"""a module for task 4

a function that returns an object
(Python data structure) represented by a JSON string
"""


import json


def from_json_string(my_str):
    """a function that returns an object
    (Python data structure) represented by a JSON string

    Args:
        my_str: string to be deserialized

    Return:
        Python object
    """
    return json.loads(my_str)
