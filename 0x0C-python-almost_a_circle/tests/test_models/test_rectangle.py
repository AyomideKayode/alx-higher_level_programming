#!/usr/bin/python3

"""
Unittest for Rectangle Class
# run with python3 -m unittest discover tests
# run with python3 -m unittest tests/test_models/test_rectangle.py
"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """TestRectangle Class"""

    def test_rectangle_initialization(self):
        """Test to check that all attributes are correctly initialized.
        """
        r = Rectangle(4, 5, 2, 3, 1)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 1)

    def test_constructor_with_id_and_without(self):
        """Test to check that the Base id parameter is set upon
        initialization if provided and if not."""
        r = Rectangle(10, 20, 30, 40, 1)
        self.assertEqual(r.id, 1)
        r = Rectangle(10, 20, 30, 40)
        self.assertEqual(r.id, 1)

    def test_with_default_attr(self):
        """Test if default attributes are set when not given.
        """
        r2 = Rectangle(3, 4)
        self.assertTrue(r2.width == 3)
        self.assertTrue(r2.height == 4)
        self.assertTrue(r2.x == 0)
        self.assertTrue(r2.y == 0)
        self.assertTrue(r2.id is not None)

    def test_height_width_with_valid_value(self):
        """Test height and width reassignment with valid values.
        """
        r = Rectangle(6, 11)
        r.width = 15
        self.assertEqual(r.width, 15)
        r = Rectangle(4, 9)
        r.height = 7
        self.assertEqual(r.height, 7)

    def test_width_with_invalid_value(self):
        """Test height and width reassignment with invalid values.
        """
        r = Rectangle(10, 20)
        with self.assertRaises(ValueError):
            r.width = -5
        r = Rectangle(10, 20)
        with self.assertRaises(ValueError):
            r.height = -5

    def test_xy_with_valid_value(self):
        """Test x and y reassignment with valid values.
        """
        r = Rectangle(10, 20, 30, 40)
        r.x = 20
        self.assertEqual(r.x, 20)
        r = Rectangle(10, 20, 30, 40)
        r.y = 8
        self.assertEqual(r.y, 8)

    def test_xy_with_invalid_value(self):
        """Test x and y reassignment with invalid values.
        """
        r = Rectangle(10, 20)
        with self.assertRaises(ValueError):
            r.x = -5
        r = Rectangle(10, 20)
        with self.assertRaises(ValueError):
            r.y = -5

    def test_with_float_string_values(self):
        """Test attributes with float and string values.
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle("invalid", 6)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(8.27, 15)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(3, "Fave")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(4, 6.45)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(3, 5, "square")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(4, 9, 2.93)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(7, 18, 4, "triangle")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(8, 10, 4, 7.38)


if __name__ == '__main__':
    unittest.main()
