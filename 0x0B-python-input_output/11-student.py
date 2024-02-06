#!/usr/bin/python3#!/usr/bin/python3
"""a module for task 11

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
            return {attr: getattr(self, attr) for attr
                    in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """Replace all attributes of the Student
        instance with the values from the provided dictionary.

        Args:
            json (dict): Dictionary containing attribute names and values.

        """
        for key, value in json.items():
            setattr(self, key, value)
