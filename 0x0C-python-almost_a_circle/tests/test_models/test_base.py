#!/usr/bin/python3

"""
Unittest for the Base class
# To execute test, run  python3 -m unittest discover tests
#To execute test, run python3 -m unittest tests/test_models/test_base.py
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """
    unittesting for Base class
    """
    def test_id(self):
        """
        # Test when id = None and when id is not None
        """
        self.assertTrue(Base(), self.id == 1)
        self.assertTrue(Base(), self.id == 2)
        self.assertTrue(Base(40), self.id == 40)
        self.assertTrue(Base(), self.id == 3)
        self.assertTrue(Base(6), self.id == 6)
        self.assertTrue(Base(), self.id == 4)
        self.assertTrue(Base(-67), self.id == -67)

    def test_arguments(self):
        """
        # Ensure type errors are raised when necessary
        """
        self.assertRaises(TypeError, Base, 3, 8)

    def test_to_json_string(self):
        """
        # Test for JSON string representation
        """
        dic_json = {}
        d_json = Base.to_json_string([dic_json])
        self.assertTrue(d_json, "[]")

        dict_json = None
        di_json = Base.to_json_string([dict_json])
        self.assertTrue(di_json, "[]")

        dict1 = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        dict2 = {'x': 5, 'y': 1, 'id': 35, 'height': 3, 'width': 6}
        json_dict = Base.to_json_string([dict1, dict2])
        self.assertTrue(json_dict, [{"x": 1, "y": 9, "id": 1, "height": 2, "width": 10}, {"x": 5, "y": 1, "id": 35, "height": 3, "width": 6}])

    def test_from_json_string(self):
        """
        # Test for JSON string to python dictionary object
        """
        st = '[{"x": 1, "y": 9, "id": 1, "height": 2, "width": 10}, {"x": 5, "y": 1, "id": 35, "height": 3, "width": 6}]'
        st_json = Base.from_json_string(st)
        self.assertTrue(st_json == [{'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}, {'x': 5, 'y': 1, 'id': 35, 'height': 3, 'width': 6}])
        self.assertTrue(type(st_json) == list)

        st1 = None
        st1_json = Base.from_json_string(st1)
        self.assertTrue(st1_json == [])

        st2 = ""
        st2_json = Base.from_json_string(st2)
        self.assertTrue(st2_json == [])

    def save_to_file(self):
        """
        # Test to write JSON string representation of a list 
        of instances to a file
        """
        r1 = Rectangle.save_to_file(None)
        with open(Rectangle.json, mode='r', encoding='utf-8') as myFile:
            self.assertEqual(myFile.read(), '[]')

        s1 = Square.save_to_file([])
        with open(Square.json, mode='r', encoding='utf-8') as myFile:
            self.assertEqual(myFile.read(), '[]')

        r2 = Rectangle(3, 2, 0, 0, 14).save_to_file()
        with open(Rectangle.json, mode='r', encoding='utf-8') as myFile:
            dic = [{"width": 3, "height": 2, "x": 0, "y": 0, "id": 14}]
            self.assertEqual(myFile.read(), dic)

    def test_create(self):
        """
        # Test create() class method that returns an instance with
        all attributes already set
        """
        r1 = Rectangle(3, 5, 1)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual(r2.__str__(), '[Rectangle] (1) 1/0 - 3/5')

    def load_from_file(self):
        """
        # Test to load JSON string to return a list of instances
        """
        r1 = Rectangle.save_to_file(None)
        r2 = Rectangle.load_from_file()
        self.assertEqual(r2, [])
        self.assertEqual(type(r2), list)
        self.assertEqual(len(r2), 0)

        s1 = Square.save_to_file(None)
        s2 = Square.load_from_file()
        self.assertEqual(s2, [])
        self.assertEqual(len(s2), 0)
        self.assertEqual(type(s2), list)

        s = Square(3, 1, 1, 8)
        Square.save_to_file([s])
        sq = Square.load_from_file()
        self.assertEqual(sq__str__(), '[Square] (8) 1/1 - 3')

