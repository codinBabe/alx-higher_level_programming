#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        """check an empty list"""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_maxend(self):
        """check a list where max value is at the end"""
        maxend = [1, 2, 3, 4]
        self.assertEqual(max_integer(maxend), 4)

    def test_maxbegin(self):
        """check a list with a beginning max value."""
        maxbegin = [4, 1, 3, 2]
        self.assertEqual(max_integer(maxbegin), 4)

    def test_middle(self):
        """check a list with max value in the middle"""
        middle = [1, 2, 8, 3, 4]
        self.assertEqual(max_integer(middle), 8)

    def test_neg_num(self):
        """Test negative number"""
        neg_num = [-5, -6, -111]
        self.assertEqual(max_integer(neg_num), -5)

    def test_one_neg_num(self):
        """Test one negative number"""
        one_neg = [-5, 6, 2]
        self.assertEqual(max_integer(one_neg), 6)

    def test_ints_and_floats(self):
        """check a list of ints and floats."""
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_float(self):
        """check a list of floats."""
        float_lst = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(float_lst), 15.2)

    def test_neg_float(self):
        """check negative floats"""
        neg_float = [-5.55, -66.66, -111.1]
        self.assertEqual(max_integer(neg_float), -5.55)

    def test_string(self):
        """check for string"""
        name = "Toyin"
        self.assertEqual(max_integer(name), 'y')

    def one_num(self):
        """check for one number"""
        num = [1]
        self.assertEqual(max_integer(num), 1)

    def test_datatypes(self):
        """ check for different data types"""
        with self.assertRaises(TypeError):
            max_integer([1, "1"])

if __name__ == '__main__':
    unittest.main()
