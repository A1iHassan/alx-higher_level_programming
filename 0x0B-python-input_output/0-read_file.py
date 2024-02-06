#!/usr/bin/python3
"""a module for task 0

a script that reads file's content and prints
it to stdout
"""


def read_file(filename=""):
    """reads a file's content and
    prints it to stdout

    Args:
        filename: file to be read
    """
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end='')
