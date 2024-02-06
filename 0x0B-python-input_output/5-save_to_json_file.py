#!/usr/bin/python3
"""a module for task 5

a function that writes an Object to
a text file, using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """a function that writes an Object to
    a text file, using a JSON representation

    Args:
        my_obj: content to be added to a file
        filename: file to add to
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
