#!/usr/bin/python3
"""a module for task 8

"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """a subclass that inherits from BaseGeometry
    
    """

    def __init__(self, width, height):
        """instantiates new instances of Rectangle
        
        Args:
            width: rectangle width
            height: rectangle height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
