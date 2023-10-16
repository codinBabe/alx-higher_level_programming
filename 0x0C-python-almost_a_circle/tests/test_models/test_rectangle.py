#!/usr/bin/python3
"""unittest for rectangle"""


import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """various rectangle test case"""
    def test_valid_creation(self):
        r = Rectangle(4, 5, 1, 2, 42)
        self.assertEqual(r.id, 42)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)

    def test_default_values(self):
        r = Rectangle(4, 5)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_invalid_width(self):
        with self.assertRaises(ValueError):
            r = Rectangle(0, 5)

    def test_invalid_height(self):
        with self.assertRaises(ValueError):
            r = Rectangle(4, -1)

    def test_invalid_x(self):
        with self.assertRaises(ValueError):
            r = Rectangle(4, 5, -1)

    def test_invalid_y(self):
        with self.assertRaises(ValueError):
            r = Rectangle(4, 5, 1, -1)

    def test_display(self):
        r = Rectangle(3, 2, 1, 1)
        expected_output = "\n ###\n ###\n"
        captured_output = io.StringIO()
        sys.stdout = captured_output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_str_representation(self):
        r = Rectangle(3, 2, 1, 1, 99)
        self.assertEqual(str(r), "[Rectangle] (99) 1/1 - 3/2")

    def test_update_method(self):
        r = Rectangle(3, 2, 1, 1, 99)
        r.update(42, 4, 5, 0, 0)
        self.assertEqual(r.id, 42)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_update_with_args(self):
        r = Rectangle(4, 5, 1, 2, 42)
        r.update(10, 6, 7, 3, 4)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 6)
        self.assertEqual(r.height, 7)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_update_with_kwargs(self):
        r = Rectangle(4, 5, 1, 2, 42)
        r.update(id=10, width=6, height=7, x=3, y=4)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 6)
        self.assertEqual(r.height, 7)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_update_with_mixed_args_and_kwargs(self):
        r = Rectangle(4, 5, 1, 2, 42)
        r.update(10, 7, 6, 3, y=4)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

if __name__ == '__main__':
    unittest.main()

class TestRectangleToDictionary(unittest.TestCase):
    def test_to_dictionary(self):
        # Test with a standard Rectangle
        r1 = Rectangle(4, 5, 1, 2, 42)
        r1_dict = r1.to_dictionary()
        expected_dict1 = {
            'id': 42,
            'width': 4,
            'height': 5,
            'x': 1,
            'y': 2
        }
        self.assertEqual(r1_dict, expected_dict1)

        # Test with a Rectangle with default values
        r2 = Rectangle(4, 5)
        r2_dict = r2.to_dictionary()
        expected_dict2 = {
            'id': 7,
            'width': 4,
            'height': 5,
            'x': 0,
            'y': 0
        }
        self.assertEqual(r2_dict, expected_dict2)

        # Test with a Rectangle with width and height
        r3 = Rectangle(4, 5, 1, 2, 3)
        r3_dict = r3.to_dictionary()
        expected_dict3 = {
            'id': 3,
            'width': 4,
            'height': 5,
            'x': 1,
            'y': 2
        }
        self.assertEqual(r3_dict, expected_dict3)

if __name__ == '__main__':
    unittest.main()
