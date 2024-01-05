#!/usr/bin/python3
"""
a module for Rectangle class

this module is dedicated to contain all ncessary data for the Rectangle class
"""


class Rectangle:
    """a new class for Rectangle data type

    Attributes:
        number_of_instances: instances created
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initializes new instances

        Args:
            width: rectangle width
            height: rectangle height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """retrieves the width

        Return:
            __width
        """
        return self._width

    @width.setter
    def width(self, value):
        """setter for __width

        Args:
            vlaue: new __width value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """getter for __height
        Returns:
            __height
        """
        return self._height

    @height.setter
    def height(self, value):
        """setter for __height

        Args:
            value: new __height value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """calculates the area of the rectangle

        Return:
            _width * "_height
        """
        return self._width * self._height

    def perimeter(self):
        """calculates the perirmeter of the rectangle

        Return:
            perimeter
        """
        if self._width > 0 and self._height > 0:
            return 2 * (self._width + self._height)
        else:
            return 0

    def __str__(self):
        """a readable form

        Return:
            string
        """
        if self._width == 0 or self._height == 0:
            return ""
        else:
            return "\n".join(["#" * self._width for _ in range(self._height)])

    def __repr__(self):
        """a reusable form with eval()

        Return:
            repr()
        """
        return f"Rectangle({self._width}, {self._height})"

    def __del__(self):
        """delete method"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
