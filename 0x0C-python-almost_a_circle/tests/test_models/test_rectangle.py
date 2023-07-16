#!/usr/bin/python3

"""
Unittest for the subclass Rectangle class
# To execute test, run  python3 -m unittest discover tests
#To execute test, run python3 -m unittest tests/test_models/test_base.py
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    unittesting for Rectangle class
    """
    def test_unnamed_argsvalues_given(self):
        """
        # Test when only unmaed argument values are passed
        """
        r1 = Rectangle(10, 5)
        self.assertTrue(r1.id is not None)
        self.assertTrue(r1.width == 10)
        self.assertTrue(r1.height == 5)
        self.assertTrue(r1.x == 0)
        self.assertTrue(r1.y == 0)

    def test_all_argsvalues_given(self):
        """
        # Test when all argument values are passed
        """
        r2 = Rectangle(10, 2, 1, 4, 12)
        self.assertTrue(r2.id == 12)
        self.assertTrue(r2.width == 10)
        self.assertTrue(r2.height == 2)
        self.assertTrue(r2.x == 1)
        self.assertTrue(r2.y == 4)

    def test_arguments(self):
        """
        # Ensure type errors are raised when necessary
        """
        self.assertRaises(TypeError, Rectangle, 3, 8, 0, 0, 2, 4)
