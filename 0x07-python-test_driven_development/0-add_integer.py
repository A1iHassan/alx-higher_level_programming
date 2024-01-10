#!/usr/bin/python3
"""module for project 0x07
"""


def add_integer(a, b=98):
    """a Function that returns the sum of two given numbers

        Args:
            a: first number (must be int or float)
            b: second number (must be int or float)

        Return:
            sum
    """
    if not isinstance((int, float), a):
        raise TypeError("a must be an integer")
    elif not isinstance((int, float), b):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
