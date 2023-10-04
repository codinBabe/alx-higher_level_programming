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

    def one_num(self):
        """check for one number"""
        num = [1]
        self.assertEqual(max_integer(num), 1)

if __name__ == '__main__':
    unittest.main()
