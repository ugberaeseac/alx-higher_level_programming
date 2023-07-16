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

    def test_invalid_arguments(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 4, 1, 3, 4, 6)
            Rectangle()
            Rectangle(6)
            Rectangle(None)

    def test_typeerror(self):
        """
        # Ensure type errors are raised when necessary
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("30", 8, 0, 0, 2)
            Rectangle([1, 2], 6)
            Rectangle(0.34, 2, 1, 0, 2)
            Rectangle(True, 5)
            Rectangle((1,), 7, 3, 9, 8)
            Rectangle({'width': '5'}, 10, 2, 4, 7)
            Rectangle(2+4j, 1, 4, 6, 9)
            Rectangle(None, 3)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(30, "8", 0, 0, 2)
            Rectangle(6, [1, 4])
            Rectangle(4, 2.7, 1, 0, 2)
            Rectangle(1, False)
            Rectangle(1, (8, 7), 3, 9, 8)
            Rectangle(3, {'height': '5'}, 2, 4, 7)
            Rectangle(2, 3+5j, 4, 6, 9)
            Rectangle(4, None, 4, 8, 9)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 1, "x", 0, 2)
            Rectangle(1, 6, [0, 0], 1, 3)
            Rectangle(24, 12, 1.5, 0, 2)
            Rectangle(1, 5, True, 0, 1)
            Rectangle(6, 7, (2,), 9, 8)
            Rectangle(5, 15, {'width': '5'}, 10, 2)
            Rectangle(9, 12, 4+3j, 6, 9)
            Rectangle(3, 4, None, 9, 8)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "3", 8)
            Rectangle(2, 5, 8, [2, 2], 6)
            Rectangle(4, 2, 1, 0.4, 2)
            Rectangle(8, 6, 4, False, 1)
            Rectangle(6, 7, 8, (1,), 7)
            Rectangle(45, 15, 3, {'width': '5'}, 7)
            Rectangle(1, 2, 3, 2+4j, 5)
            Rectangle(8, 12, 4, None, 4)

    def test_valueerror(self):
        """
        # Ensure value errors are raised when necessary
        """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 4)
            Rectangle(-3, 6, 0, 0, 3)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -1, 1, 1, 1)
            Rectangle(3, 0, 2, 0, 6)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -4, 3, 9)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 5, 0, -46, 3)

    def test_area(self):
        """
        # Test the area method of the Rectange class
        """
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(2, 10).area(), 20)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)
        self.assertEqual(Rectangle(2, 7, 1, 6).area(), 14)

    def test_str(self):
        """
        # Test the __str__ method or str()
        """
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")

    def test_update(self):
        """
        # Test the update method that assigns an arg to each attribute
        """
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")

        r1.update(10, 10, 10, 10, 10)
        self.assertEqual(r1.__str__(), "[Rectangle] (10) 10/10 - 10/10")

        r1.update(89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 10/10")

        r1.update(89, 2)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/10")

        r1.update(89, 2, 3)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/3")

        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/10 - 2/3")

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")

        r1.update()
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")

        """
        # Test for kwargs (key/value) arguments to attributes
        """
        r1 = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(r1.__str__(), "[Rectangle] (10) 10/10 - 10/10")

        r1.update(id=20)
        self.assertEqual(r1.__str__(), "[Rectangle] (20) 10/10 - 10/10")

        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 3/1 - 2/10")
