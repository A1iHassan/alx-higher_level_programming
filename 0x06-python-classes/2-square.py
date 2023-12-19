#!/usr/bin/python3

"""a module for Square class.

this module defines the class Square with all of its necessary attributes
"""


class Square:
    """class defines a square.

    this class holds all necessary attribute for defining a square.

    Attributes:
        __size: size of the square.
    """

    def __init__(self, size=0):
        """initializes an instance.

        Args:
            size: gives the square size.
        """
        if not type(size) is int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
