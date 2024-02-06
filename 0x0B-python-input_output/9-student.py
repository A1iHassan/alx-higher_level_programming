#!/usr/bin/python3
"""a module for task 9

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

    def to_json(self):
        """retrieves a dictionary representation of
        a Student instance

        Return:
            a type of dict
        """
        instance_dict = self.__dict__

        for key, value in instance_dict.items():
            if isinstance(value, (list, dict, str, int, bool)):
                continue
            elif isinstance(value, (tuple, set)):
                instance_dict[key] = list(value)
            elif hasattr(value, '__dict__'):
                instance_dict[key] = self.to_json(value)
        
        return instance_dict
