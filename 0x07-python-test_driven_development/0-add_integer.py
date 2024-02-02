#!/usr/bin/python3
"""Module for add_integer"""


def add_integer(a, b=98):
    """Adds two given integers.

    Args:
        a: first int.
        b: second int.

    Raises:
        TypeError: if a, b are neither int nor float.

    Returns:
        sum of a and b.
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
