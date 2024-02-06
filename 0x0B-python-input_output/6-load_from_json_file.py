#!/usr/bin/python3
"""a module for task 6

a function that creates an Object from a
“JSON file”
"""


import json


def load_from_json_file(filename):
    """a function that creates an Object from a
    “JSON file”

    Args:
        filename: file to extract object from

    Return:
        Python object
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
