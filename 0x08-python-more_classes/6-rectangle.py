#!/usr/bin/python3
"""a module for the Rectangle class"""


class Rectangle:
    """a class for the Rectangle data type that contains all of
    the attributes of a rectangle

    Attributes:
        number_of_instances:
    Initialized to 0
    Incremented during each new instance instantiation
    Decremented during each instance deletion
    """

    number_of_instances = 0

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
            Rectangle.number_of_instances += 1

    def __str__(self):
        """returns a humen readable
        representation of the rectangle

        Return:
            # or an empty string
        """
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            x = ""
            for i in range(self.__height):
                x += "#" * self.__width + "\n"
            return x.rstrip('\n')

    def __repr__(self):
        """returns a string format to be used dinamicly

        Return:
            formal representation
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """called when deleting an instance of the class"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """a getter property for the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """a setter property for the width attribute

        Args:
            value: width to be set
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """a getter property for the height attribute

        Return:
            __width
        """
        return self.__height

    @height.setter
    def height(self, value):
        """a setter property for the height attribute

        Args:
            value: height to be set
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """calculates the rectangle's area

        Return:
            width x height
        """
        return self.__width * self.__height

    def perimeter(self):
        """calculates the perimeter of the rectangle,
        if one dimention is 0, returns 0

        Return:
            2 x (width + height)
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)
