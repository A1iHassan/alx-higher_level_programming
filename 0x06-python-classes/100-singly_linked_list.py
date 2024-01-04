#!/usr/bin/python3

"""a module for Node and SinglyLinkedList classes.

this module contains the deffinition and data of both Node class and SinglyLinkedList class
with all of their attributes
"""

class Node:
    """a list node.

    a linked list node that contains data and an indicator for the next node.

    Attributes:
        __data: node's data.
        __next_node: an indecator for the next node.
    """

    def __init__(self, data, next_node=None):
        """initializes new instances.

        Args:
            data: new node's data.
            next_node: next node in order.
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        elif not isinstance(next_node, (None, Node)):
            raise TypeError("next_node must be a Node object")
        else:
            self.__data = data
            self.__next_node = next_node

    @property
    def data(self):
        """a getter for __data.

        Return:
            __data.
        """
        return self.__data
    
    @property
    def next_node(self):
        """a getter for __next_node.

        Return:
            __next_node.
        """
        return self.__next_node
    
    @data.setter
    def data(self, value):
        """a setter for __data

        Args:
            value: an int
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @next_node.setter
    def next_node(self, value):
        """a setter for __next_node.

        Args:
            value: a Node or None
        """
        if not isinstance(value, (None, Node)):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """a linked list class

    this class represents a linked list structure and mechanisim.

    Attributes:
        head: begining of the list.
    """


    def __init__(self):
        """initializes a new instance.
        """
