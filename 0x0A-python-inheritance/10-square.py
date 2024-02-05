#!/usr/bin/python3
"""a module for task 10"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a subclass from Rectangle"""

    def __init__(self, size):
        """instantiates new instances of Square"""
        super.integer_validator(size)
        self.__size = size

    def area(self):
        """calculates the area
        over-writes the super-class's method 'area()'
        """
        return self.__size * self.__size
