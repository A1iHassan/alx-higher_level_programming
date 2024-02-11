#!/usr/bin/python3
"""third module in this python pakage

contains the Square class with all its attributes
"""


from rectangle import Rectangle


class Square(Rectangle):
    """a subclass that inherits form the
    super class Rectangle

    Attributes:
        all attributes are inherited from the super
        class Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """instantiates new instances of Square

        Args:
            size: holds the width/height values
            x: sets the inherited __x attribute
            y: sets the inherited __y attribute
            id: defaulted to None, sets the
            inhetited id attribute
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns an informal representation of the
        instance

        Return:
            str type
        """
        return f"[Square] ({self.id}) {self.__x}/{self.__y} - {self.__width}"

    def to_dictionary(self):
        """returns a dictionary representation of
        the instance

        Return:
            dict
        """
        return {"x": self.__x, "y": self.__y, "id": self.__id,
                "size": self.__width}

    @property
    def size(self):
        """a getter for the size (width/height) value

        Return:
            __width
        """
        return self.__width

    @property
    def size(self, value):
        """a setter for the size (width/height) value

        Args:
            value: to update width/height
        """
        super().width(value)
        super().height(value)

    def update(self, *args, **kwargs):
        """used to update instance's attributes

        Args:
           args: a variable number of inputs list
        """
        i = len(args)
        if i == 0:
            if "size" in kwargs:
                self.__height = kwargs["size"]
                self.__width = kwargs["size"]
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
                self.__height = args[1]
                self.__width = args[1]
            if i > 2:
                self.__x = args[2]
            if i > 3:
                self.__y = args[3]
