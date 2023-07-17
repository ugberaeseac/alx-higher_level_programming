#!/usr/bin/python3

"""
Module: base
contains super class Base
Contains the class attribute __nb_objects
"""


import json


class Base:
    """
    defines the Base class

    Class Attributes:
        __nb_objects

    Methods:
        __init__(self, id=None)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize attribute id, increment __nb_objects
        if id is None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            list_dictionaries = []
        else:
            return json.dumps(list_dictionaries)
