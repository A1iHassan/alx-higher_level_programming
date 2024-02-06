#!/usr/bin/python3
"""a module for task 2

a function that appends a string at the end of a text
file (UTF8) and returns the number of characters added
"""


def append_write(filename="", text=""):
    """a function that appends a string at the end of a text
    file (UTF8) and returns the number of characters added

    Args:
        filename: file to append to
        text: content to be appended

    Return:
        number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
