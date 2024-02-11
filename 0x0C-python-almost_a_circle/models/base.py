#!/usr/bin/python3
"""first module in this python pakage

contains the Base class with all its attributes
"""

import json



class Base:
    """This class will be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all future classes
    and to avoid duplicating the same code

    Attributes:
        __nb_objects: private class attribute
        id: public instance attribute
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """instantiates new instances of Base

        Args:
            id: sets the instance attribute id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON representation of a list
        of dictionaries

        Args:
            list_dictionaries: a list of dictionaries

        Return:
            JSON string
        """
        if list_dictionaries and len(list_dictionaries) > 0:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string
        representation json_string

        Args:
            json_string: string representing a list of dictionaries
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation
        of list_objs to a file

        Args:
            list_objs: list of instances who inherits of Base
        """
        with open({cls.__name__ + ".json"}, 'w', encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set

        Args:
            dictionary: values to set the attributes
        """
        dummy = cls.__init__(0, 0, 0, 0)
        dummy.update(None, dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances

        Return:
            instances of the calling class
        """
        try:
            with open({cls.__name__ + ".josn"}, 'r', encoding="utf-8") as f:
                list_string = f.read()
                list_instances = cls.from_json_string(list_string)
                return [cls.create(i) for i in list_instances]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """saves a list of instances to a file as
        a CSV text
    
        Args:
            list_objs: list of instances of the same type
        """
        with open(cls.__name__ + ".csv", 'w', encoding="utf-8") as f:
            if cls.__name__ == "Rectangle":
                for i in list_objs:
                    line = f"{i['id']},{i['width']},{i['height']},{i['x']},{i['y']}\n"
                    f.write(line)
            elif cls.__name__ == "Square":
                for i in list_objs:
                    line = f"{i['id']},{i['size']},{i['x']},{i['y']}"
                    f.write(line)

    @classmethod
    def load_from_file_csv(cls):
        """loads a list of instances from a file
        containing CSV data

        Return:
            list of intances
        """
        try:
            with open(cls.__name__ + ".csv", 'r', encoding="utf-8") as f:
                list_string = f.read()
                list_instances = list_string.split(',')
                dummy = cls.__init__(0, 0, 0, 0)
                return [dummy.update(None, i) for i in list_instances]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles
        and Squares

        Args:
            list_rectangles: ...
            list_squares: ...
        """
        import turtle


        screen = turtle.Screen()
        t = turtle.Turtle()

        t.penup()
        t.left(90)
        t.forward(500)
        t.left(90)
        t.forward(500)
        t.right(180)
        t.pendown()
        for i in list_rectangles:
            t.penup()
            t.forward(i.x())
            t.right(90)
            t.forward(i.y())
            t.left(90)
            t.pendown()
            t.forward(i.width())
            t.right(90)
            t.forward(i.height())
            t.right(90)
            t.forward(i.width())
            t.right(90)
            t.forward(i.height())
            t.right(90)
        for i in list_squares:
            t.penup()
            t.forward(i.x())
            t.right(90)
            t.forward(i.y())
            t.left(90)
            t.pendown()
            t.forward(i.width())
            t.right(90)
            t.forward(i.height())
            t.right(90)
            t.forward(i.width())
            t.right(90)
            t.forward(i.height())
            t.right(90)
        screen.mainloop()
