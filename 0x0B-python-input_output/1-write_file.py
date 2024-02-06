#!/usr/bin/python3
"""a module for task 1

a function that writes a string to a text file
(UTF8) and returns the number of characters written
"""


def write_file(filename="", text=""):
    """a function that writes a string to a text file
    (UTF8) and returns the number of characters written

    Args:
        filename: file to write to
        text: content to be writen

        Return:
            number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
