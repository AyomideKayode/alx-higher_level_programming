#!/usr/bin/python3

"""
Unittest for Square Class
# run with python3 -m unittest discover tests
# run with python3 -m unittest tests/test_models/test_square.py
"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_constructor(self):
        s = Square(5, 2, 3, 42)
        self.assertEqual(s.id, 42)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_constructor_defaults(self):
        s = Square(5)
        self.assertEqual(s.id, 4)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_args_count(self):
        """Test to check for exception when too many args are passed.
        """
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5, 6, 7)
        """Test to check for exception when too little args are passed.
        """
        with self.assertRaises(TypeError):
            Square()
            Square(None)

    def test_attribute_validation(self):
        """Test attributes are validated before set.
        And exceptions are being raised."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("10")
            Square([10, (3)])
            Square({20, '7'})
            Square({"d": 24})
            Square((6, 10), 8)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)
            Square(9).size(-9)

    def test_str_print(self):
        """Test the __str__ method to verify that it prints out the string
        reprsentation of the Square attributes.
        """
        s = Square(5, 2, 3, 42)
        expected_output = "[Square] (42) 2/3 - 5"
        self.assertEqual(str(s), expected_output)

    def test_class(self):
        """Test that the Square instance class is initialized.
        """
        s = Square(24)
        self.assertEqual(type(s), Square)


if __name__ == '__main__':
    unittest.main()
