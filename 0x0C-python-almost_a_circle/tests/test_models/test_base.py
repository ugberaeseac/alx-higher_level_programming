#!/usr/bin/python3

"""
Unittest for the Base class
# To execute test, run  python3 -m unittest discover tests
#To execute test, run python3 -m unittest tests/test_models/test_base.py
"""


import unittest
from models.base import Base
from models.base import Rectangle


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
        self.assertTrue(
                json_dict, [{"x": 1, "y": 9, "id": 1, "height": 2, "width": 10},
                    {"x": 5, "y": 1, "id": 35, "height": 3, "width": 6}])
