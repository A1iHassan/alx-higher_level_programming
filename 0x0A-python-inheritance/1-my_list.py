#!/usr/bin/python3
"""a module for Class myList
"""


class MyList(list):
    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        sorted_list = sorted(self)
        print(sorted_list)