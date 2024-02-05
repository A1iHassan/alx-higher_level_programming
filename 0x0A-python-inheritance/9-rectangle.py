#!/usr/bin/python3
"""a module for task 9

"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a subclass that inherits from BaseGeometry
    yes
    """

    def __init__(self, width, height):
        """instantiates new instances of Rectangle

        Args:
            width: rectangle width
            height: rectangle height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """returns a readable string

        Return:
            a str type
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
    
    def area(self):
        """calculates the area
        over-writes the super-class's method 'area()'
        """
        return self.__height * self.__width
