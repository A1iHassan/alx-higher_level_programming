#!/usr/bin/python3
"""a module for task 12"""


class MyInt(int):
    """a subclass from int"""

    def __eq__(self, value):
        """will behave as the != operator"""
        return super().__ne__(value)

    def __ne__(self, value):
        """will behave as the == operator"""
        return super().__eq__(value)
