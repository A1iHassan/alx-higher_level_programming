#!/user/bin/python3
"""a module for task 12"""


class MyInt(int):
    """a subclass from int"""

    def __eq__(self, __value: object):
        """will behave as the != operator"""
        return self > __value or self < __value

    def __ne__(self, __value: object):
        """will behave as the == operator"""
        return not self > __value and not self < __value
