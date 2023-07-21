#!/usr/bin/python3

"""
Module: base
contains super class Base
Contains the class attribute __nb_objects
"""


import json
import csv


class Base:
    """
    defines the Base class

    Class Attributes:
        __nb_objects

    Methods:
        __init__(self, id=None)
        to_json_string(list_dictionaries)
        save_to_file(cls, list_objs)
        from_json_string(json_string)
        create(cls, **dictionary)
        load_from_file(cls)
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
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of a list of Base instance
        """
        objs_list = []

        if list_objs is not None:
            for objs in list_objs:
                objs_list.append(cls.to_dictionary(objs))

        filename = cls.__name__ + ".json"
        with open(filename, mode='w', encoding='utf-8') as myFile:
            myFile.write(cls.to_json_string(objs_list))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """
        class method that return an instance with attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(2, 4)
        if cls.__name__ == "Square":
            dummy = cls(4)

        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """
        return a list of instances
        """
        a_list = []
        file_name = cls.__name__ + ".json"

        try:
            with open(file_name, mode='r', encoding='utf-8') as myFile:
                readFile = myFile.read()
                objs = cls.from_json_string(readFile)
            for instance in objs:
                a_list.append(cls.create(**instance))

        except (FileNotFoundError):
            pass
        return (a_list)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        save/serialize to csv file
        """
        filename = cls.__name__ + ".csv"
        with open(filename, mode='w', newline='') as csvFile:
            csv_write = csv.writer(csvFile)

            for row in list_objs:
                if cls.__name__ == "Rectangle":
                    csv_write.writerow(
                            [row.id, row.width, row.height, row.x, row.y])
                if cls.__name__ == "Square":
                    csv_write.writerow([row.id, row.size, row.x, row.y])

    @classmethod
    def load_from_file_csv(cls):
        list_objs = []
        filename = cls.__name__ + ".csv"
        with open(filename, 'r', newline='') as csvFile:
            csv_read = csv.reader(csvFile)
            for row in csv_read:
                if cls.__name__ == "Rectangle":
                    dictt = {"id": int(row[0]), "width": int(row[1]),
                            "height": int(row[2]), "x": int(row[3]),
                            "y": int(row[4])}
                if cls.__name__ == "Square":
                    dictt = {"id": int(row[0]), "size": int(row[1]),
                            "x": int(row[2]), "y": int(row[3])}
                obj = cls.create(**dictt)
                list_objs.append(obj)
        return (list_objs)
