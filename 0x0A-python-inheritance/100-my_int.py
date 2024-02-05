#!/user/bin/python3
"""a module for task 12"""


class MyInt(int):
    """a subclass from int"""

    def __eq__(self, value):
        """will behave as the != operator"""
        return self > value or self < value

    def __ne__(self, value):
        """will behave as the == operator"""
        return not self > value and not self < value
