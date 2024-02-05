#!/usr/bin/python3
"""a module for task 1"""


class MyList(list):
    """a subclass"""

    def print_sorted(self):
        """prints the list elements in ascending order"""
        print(sorted(self))
