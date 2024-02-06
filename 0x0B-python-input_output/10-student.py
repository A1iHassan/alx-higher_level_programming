#!/usr/bin/python3
"""a module for task 10

contains a custom Class with all its attributes
"""


class Student:
    """a class for student

    Attributes:
        first_name: student's first name
        last_name: student's last name
        age: student's age
    """

    def __init__(self, first_name, last_name, age):
        """instantiates new Student instances

        Args:
            first_name: ...
            last_name: ...
            age: ...
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of
        a Student instance

        Return:
            a type of dict
        """
        if attrs is None:
            return self.__dict__
        else:
            for attr in attrs:
                if not hasattr(self, attr):
                    attrs.pop(attr)
            return {attr: getattr(self, attr) for attr in attrs}
