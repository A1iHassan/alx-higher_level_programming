#!/usr/bin/python3
"""second module in this python pakage

contains the Rectangle class with all its attributes
"""


from base import Base


class Rectangle(Base):
    """a subclass that inherits from the Base class

    Attributes:
        __width: private instance attribute
        __height: private instance attribute
        __x: private instance attribute
        __y: private instance attribute
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """instantiates new instances of Rectangle

        calls the super class __init__ method

        Args:
            width: sets the __width attribute
            height: sets the __height attribute
            x: sets the __x attribute
            y: sets the __y attribute
            id: defaulted to None, sets the
            inhetited id attribute
        """
        super().__init__(id)
        arr = {"width": width, "height": height, "x": x, "y": y}
        for key, value in arr:
            if not isinstance(value, int):
                raise TypeError(f"{key} must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        elif height <= 0:
            raise ValueError("height must be > 0")
        elif x < 0:
            raise ValueError("x must be >= 0")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def __str__(self):
        """returns an informal representation of the
        instance

        Return:
            str type
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} \
            - {self.__width}/{self.__height}"

    def to_dictionary(self):
        """returns a dictionary representation of
        the instance

        Return:
            dict
        """
        return {"x": self.__x, "y": self.__y, "id": self.id,
                "height": self.__height, "width": self.__width}

    @property
    def width(self):
        """a getter method for private attribute __width

        Return:
            self.__width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """a setter method for private attribute __width

        Args:
            value: to set the __width attribute
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """a getter method for private attribute __height

        Return:
            self.__height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """a setter method for private attribute __height

        Args:
            value: to set the __height attribute
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """a getter method for private attribute __x

        Return:
            self.__x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """a setter method for private attribute __x

        Args:
            value: to set the __x attribute
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        """a getter method for private attribute __y

        Return:
            self.__y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """a setter method for private attribute __y

        Args:
            value: to set the __y attribute
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """calculates the area of the Rectangle

        Retun:
            int
        """
        return self.__height * self.__width

    def display(self):
        """prints out the Rectangle instance"""
        print('\n' * (self.__y - 1))
        for _ in range(self.__height):
            print(' ' * self.__x + "#" * self.__width)

    def update(self, *args, **kwargs):
        """used to update instance's attributes

        Args:
           args: a variable number of inputs list
        """
        i = len(args)
        if i == 0:
            if "width" in kwargs:
                self.__width = kwargs["width"]
            if "height" in kwargs:
                self.__height = kwargs["height"]
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "x" in kwargs:
                self.__x = kwargs["x"]
            if "y" in kwargs:
                self.__y = kwargs["y"]
        else:
            if i > 0:
                self.id = args[0]
            if i > 1:
                self.__width = args[1]
            if i > 2:
                self.__height = args[2]
            if i > 3:
                self.__x = args[3]
            if i > 4:
                self.__y = args[4]
