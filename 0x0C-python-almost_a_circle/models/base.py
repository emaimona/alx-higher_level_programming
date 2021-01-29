#!/usr/bin/python3
"""Module for Base Class"""
import json

class Base:
    """Represent the base model

    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of

        Args:
            list_dictionaries (list): a list of dictionaries
        Return:
             If list_dictionaries is None or empty, return the string: "[]"
             Otherwise, return the JSON string representation of
             list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return []
        return json.dumps(list_dictionaries)
