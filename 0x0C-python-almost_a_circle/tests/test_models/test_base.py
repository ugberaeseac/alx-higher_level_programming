#!/usr/bin/python3

"""
Unittest for the Base class
# To execute test, run  python3 -m unittest discover tests
#To execute test, run python3 -m unittest tests/test_models/test_base.py
"""


import unittest
from models.base import Base


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
