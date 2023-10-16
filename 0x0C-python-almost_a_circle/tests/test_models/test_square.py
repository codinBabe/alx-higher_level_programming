#!/usr/bin/python3



"""unittest for square"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_init(self):
        s = Square(5, 1, 2, 42)
        self.assertEqual(s.id, 42)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)

    def test_init_defaults(self):
        s = Square(5)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_update_args(self):
        s = Square(5, 1, 2, 42)
        s.update(10, 6, 3, 4)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 6)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_update_kwargs(self):
        s = Square(5, 1, 2, 42)
        s.update(id=10, size=6, x=3, y=4)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 6)
        self.assertEqual(s.width, 6)
        self.assertEqual(s.height, 6)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_to_dictionary(self):
        s = Square(5, 1, 2, 42)
        s_dict = s.to_dictionary()
        expected_dict = {
            'id': 42,
            'size': 5,
            'x': 1,
            'y': 2
        }
        self.assertEqual(s_dict, expected_dict)

if __name__ == '__main__':
    unittest.main()

