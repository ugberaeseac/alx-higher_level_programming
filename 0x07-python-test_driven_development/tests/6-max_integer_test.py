#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    """
    To test -->> python3 -m unittest -v tests.6-max_integer_test
    """


    def test_docstring(self):
        functionDoc = __import__('6-max_integer').max_integer.__doc__
        self.assertTrue(len(functionDoc) > 1)

    def test_module_docstring(self):
        moduleDoc = __import__('6-max_integer').__doc__
        self.assertTrue(len(moduleDoc) > 1)

    def test_integers_and_floats(self):
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([11, 3, 8, 7]), 11)
        self.assertEqual(max_integer([0, 1, 2, -4]), 2)
        self.assertEqual(max_integer([-0.5, -12.5]), -0.5)
        self.assertEqual(max_integer([10, -10, 10]), 10)
        self.assertEqual(max_integer([{1, 9}, {2}, {3}]), {1, 9})

    def test_strings(self):
        self.assertEqual(max_integer(['a', 'e', 'i', 'o', 'u']), 'u')
        self.assertEqual(max_integer("47748240"), '8')
        self.assertEqual(max_integer("abcdmnopwxyz"), 'z')
        self.assertEqual(max_integer(["ijk", 'y']), 'y')

    def test_lists(self):
        self.assertEqual(max_integer([[1, 2], [1, 3]]), [1, 3])

    def test_raises(self):
        with self.assertRaises(TypeError):
            max_integer([30, "ALX", "SE"])
        with self.assertRaises(TypeError):
            max_integer({5, 6}, {8, 9, 4})
        with self.assertRaises(TypeError):
            max_integer([None, True])
        with self.assertRaises(TypeError):
            max_integer({-1, 0, 3, 9, 51})

    def test_None(self):
        self.assertIsNone(max_integer([]), None)
        self.assertIsNone(max_integer(), None)
        self.assertIsNone(max_integer([None]), None)

if __name__ == "__main__":
    unittest.main()
