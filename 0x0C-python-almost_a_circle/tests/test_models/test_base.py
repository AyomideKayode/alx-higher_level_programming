#!/usr/bin/python3

"""
Unittest for Base Class
# run with python3 -m unittest discover tests
# run with python3 -m unittest tests/test_models/test_base.py
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_module_docstring(self):
        """
        Test if the module docstring is present.
        """
        self.assertTrue(len(__doc__) >= 1)

    def test_class_docstring(self):
        """
        Test if the Base class docstring is present.
        """
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_id_assignment_with_id_argument(self):
        """Test to check whether the id attribute is assigned correctly
        when an id argument is provided during initialization.
        """
        base_instance = Base(42)
        self.assertEqual(base_instance.id, 42)
        my_base = Base(25)
        self.assertEqual(my_base.id, 25)

    def test_id_assignment_without_id_argument(self):
        """Test checks whether the id attribute is assigned correctly
        when no id argument is provided during initialization.
        And that it also increments.
        """
        base_instance = Base()
        base_instance2 = Base()
        self.assertEqual(base_instance.id, 1)
        self.assertEqual(base_instance2.id, 2)

    def test_id_assignment_with_string(self):
        """Test to check if the id attribute would work correctly when
        a string type id is provided during initialization.
        """
        base_string = Base("Kazzywiz")
        self.assertEqual(base_string.id, "Kazzywiz")
        base_string2 = Base("Unittest")
        self.assertEqual(base_string2.id, "Unittest")

    def test_more_than_one_arg(self):
        """Test to confirm that Base class does indeed raises
        a TypeError if we pass in more than one args as id.
        """
        with self.assertRaises(TypeError):
            Base(42, 25)

    def test_type(self):
        self.assertEqual(type(Base), type)

    def test_id_reassignment(self):
        """Test to check if id can be reassigned a new value
        after initial initialization.
        """
        switch = Base(25)
        switch.id = 42
        self.assertEqual(42, switch.id)


if __name__ == '__main__':
    unittest.main()
