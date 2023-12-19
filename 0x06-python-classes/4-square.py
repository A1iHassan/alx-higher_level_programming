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

    @property
    def size(self):
        """a getter for __size.

        Return:
            __size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """sets __size.

        Args:
            vlaue: desired set value
        """
        if not type(value) is int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """returns the square area.

        calculates the square's area from its saved size value.

        Return:
            square area
        """
        return self.__size**2
