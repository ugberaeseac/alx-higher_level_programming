#!/usr/bin/python3

"""
Unittest for the subclass Square class
# To execute test, run  python3 -m unittest discover tests
# To execute test, run python3 -m unittest tests/test_models/test_square.py
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO
import sys


class TestSquare(unittest.TestCase):
    """
    unittesting for Square class
    """
    def test_unnamed_argsvalues_given(self):
        """
        # Test when only un-named argument values are passed
        """
        s = Square(10, 5)
        self.assertTrue(s.id is not None)
        self.assertTrue(s.size == 10)
        self.assertTrue(s.width == 10)
        self.assertTrue(s.height == 10)
        self.assertTrue(s.x == 5)
        self.assertTrue(s.y == 0)

        s1 = Square(6)
        self.assertTrue(s1.id is not None)
        self.assertTrue(s1.size == 6)
        self.assertTrue(s1.width == 6)
        self.assertTrue(s1.height == 6)
        self.assertTrue(s1.x == 0)
        self.assertTrue(s1.y == 0)

    def test_all_argsvalues_given(self):
        """
        # Test when all argument values are passed
        """
        s2 = Square(10, 2, 1, 4)
        self.assertTrue(s2.id == 4)
        self.assertTrue(s2.size == 10)
        self.assertTrue(s2.width == 10)
        self.assertTrue(s2.height == 10)
        self.assertTrue(s2.x == 2)
        self.assertTrue(s2.y == 1)

    def test_invalid_arguments(self):
        with self.assertRaises(TypeError):
            Square(2, 4, 1, 3, 4, 6)
            Square()
            Square(None)

    def test_typeerror(self):
        """
        # Ensure type errors are raised when necessary
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("30", 8, 0, 2)
            Square([1, 2], 6)
            Square(0.34, 2, 1, 6)
            Square(True, 5)
            Square((1,), 7, 3, 8)
            Square({'width': '5'}, 10, 2, 4)
            Square(2+4j, 1, 4, 6)
            Square(None, 3)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, "x", 0, 2)
            Square(1, [0, 0], 1, 3)
            Square(24, 1.5, 0, 2)
            Square(1, True, 0, 1)
            Square(6, (2,), 9, 8)
            Square(5, {'width': '5'}, 10, 2)
            Square(9, 4+3j, 6, 9)
            Square(3, None, 9, 8)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "3", 8)
            Square(2, 5, [2, 2], 6)
            Square(4, 2, 0.4, 2)
            Square(8, 6, False, 1)
            Square(6, 7, (1,), 7)
            Square(45, 15, {'width': '5'}, 7)
            Square(1, 2, 2+4j, 5)
            Square(8, 12, None, 4)

    def test_valueerror(self):
        """
        # Ensure value errors are raised when necessary
        """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 4)
            Square(-3, 6, 0, 3)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -4, 3, 9)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(3, 5, -46, 3)

    def test_area(self):
        """
        # Test the area method of the Rectange class
        """
        self.assertEqual(Square(3).area(), 9)
        self.assertEqual(Square(2, 10).area(), 4)
        self.assertEqual(Square(8, 0, 0, 12).area(), 64)
        self.assertEqual(Square(7, 7, 1, 6).area(), 49)

    def test_str_square(self):
        """
        # Test the __str__ method or str()
        """
        s1 = Square(4, 2, 1, 12)
        self.assertEqual(s1.__str__(), "[Square] (12) 2/1 - 4")

        s1.size = 40
        self.assertEqual(s1.__str__(), "[Square] (12) 2/1 - 40")

    def test_update_square(self):
        """
        # Test the update method that assigns an arg to each attribute
        """
        s1 = Square(4, 2, 1, 12)
        self.assertEqual(s1.__str__(), "[Square] (12) 2/1 - 4")

        s1.update(10, 10, 10, 10)
        self.assertEqual(s1.__str__(), "[Square] (10) 10/10 - 10")

        s1.update(89)
        self.assertEqual(s1.__str__(), "[Square] (89) 10/10 - 10")

        s1.update(89, 2)
        self.assertEqual(s1.__str__(), "[Square] (89) 10/10 - 2")

        s1.update(89, 2, 3)
        self.assertEqual(s1.__str__(), "[Square] (89) 3/10 - 2")

        s1.update(89, 2, 3, 4)
        self.assertEqual(s1.__str__(), "[Square] (89) 3/4 - 2")

        s1.update()
        self.assertEqual(s1.__str__(), "[Square] (89) 3/4 - 2")

        """
        # Test for kwargs (key/value) arguments to attributes
        """
        s1 = Square(10, 10, 10, 10)
        self.assertEqual(s1.__str__(), "[Square] (10) 10/10 - 10")

        s1.update(id=20)
        self.assertEqual(s1.__str__(), "[Square] (20) 10/10 - 10")

        s1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(s1.__str__(), "[Square] (89) 3/1 - 2")

    def test_display_square(self):
        """
        # Test display() method without handling x and y
        """
        with StringIO() as output:
            output = StringIO()
            sys.stdout = output
            s1 = Square(2).display()
            sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "##\n##\n")

        with StringIO() as output:
            output = StringIO()
            sys.stdout = output
            s1 = Square(4).display()
            sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "####\n####\n####\n####\n")

        """
        # Test display () method handling x and y
        """
        with StringIO() as output:
            output = StringIO()
            sys.stdout = output
            s1 = Square(2, 3, 2, 2).display()
            sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "\n\n   ##\n   ##\n")

        with StringIO() as output:
            output = StringIO()
            sys.stdout = output
            s1 = Square(3, 2, 3, 1).display()
            sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "\n\n\n  ###\n  ###\n  ###\n")

    def test_to_dictionary_square(self):
        """
        # Test for dictionary representation
        """
        s1 = Square(6, 3, 2, 9)
        s1 = s1.to_dictionary()
        self.assertEqual(type(s1), dict)

        s2 = Square(1, 3, 0, 1)
        s2.update(**s1)
        self.assertEqual(s2.__str__(), "[Square] (9) 3/2 - 6")
