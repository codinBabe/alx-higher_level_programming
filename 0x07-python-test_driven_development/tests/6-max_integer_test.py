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

if __name__ == '__main__':
    unittest.main()
