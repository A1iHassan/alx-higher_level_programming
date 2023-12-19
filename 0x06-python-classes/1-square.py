#!/usr/bin/python3

"""a module for Square class

this module contains the deffinition of the Square class and all its attributes
"""


class Square:
    """a class that defines square

    this class defines a square with all its necessary attributes

    Attributes:
        __size: square size.
    """

    def __init__(self, size):
        """initializes class instances

        Args:
            size: sets the _size attribute
        """
        self.__size = size
