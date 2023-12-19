#!/usr/bin/python3

"""a module for Square class.

this module defines the class Square with all of its necessary attributes
"""


class Square:
    """class defines a square.

    this class holds all necessary attribute for defining a square.

    Attributes:
        __size: size of the square.
        __position: position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """initializes an instance.

        Args:
            size: gives the square size.
            position: a tupple of two positive integers.
        """
        if not type(size) is int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif (not (isinstance(position, tuple) and
                      len(position) == 2 and
                      position[0] > 0 and position[1] > 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__size = size
            self.__position = position

    @property
    def size(self):
        """a getter for __size.

        Return:
            __size.
        """
        return self.__size

    @property
    def position(self):
        """a getter for __position.

        Return:
            __position.
        """
        return self.__position

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

    @position.setter
    def position(self, value):
        """a setter for __posisiotn.

        Args:
            value: a tupple of two positive integers.
        """
        if not isinstance(value, tuple) or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            __position = value

    def area(self):
        """returns the square area.

        calculates the square's area from its saved size value.

        Return:
            square area
        """
        return self.__size**2

    def my_print(self):
        """print the square.

        visualizes the square using the # character
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
