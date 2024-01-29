#!/usr/bin/python3
"""a module for the Rectangle class"""


class Rectangle:
    """a class for the Rectangle data type that contains all of
    the attributes of a rectangle"""

    def __init__(self, width=0, height=0):
        """function called when creatint a new instance

        Args:
            width: rectangle width
            height: rectangle height
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__width = width
            self.__height = height
