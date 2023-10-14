#!/usr/bin/python3

"""
Unittest for Base Class
# run with python3 -m unittest discover tests
# run with python3 -m unittest tests/test_models/test_base.py
"""

import unittest
import json
from models import base
from models import rectangle
Base = base.Base
Rectangle = rectangle.Rectangle



class TestBase(unittest.TestCase):
    """TestBase Class"""

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

    def test_to_json_string(self):
        list_of_dicts = [{'id': 1, 'name': 'Joy'}, {'id': 2, 'name': 'Bob'}]
        output = '[{"id": 1, "name": "Joy"}, {"id": 2, "name": "Bob"}]'
        result = Base.to_json_string(list_of_dicts)
        self.assertEqual(result, output)
        self.assertTrue(type(result) == str)

    def test_to_json_string_empty_list(self):
        list_of_dicts = []
        expected_output = '[]'
        json_str = Base.to_json_string(list_of_dicts)
        self.assertEqual(json_str, expected_output)

    def test_to_json_string_none(self):
        list_of_dicts = None
        expected_output = '[]'
        json_str = Base.to_json_string(list_of_dicts)
        self.assertEqual(json_str, expected_output)

    def test_save_to_file(self):
        """Test save to file with instance that inherited from Base.
        """
        r = Rectangle(10, 7, 2, 8, 99)
        r2 = Rectangle(2, 4, 2, 2, 98)
        Rectangle.save_to_file([r, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(
                json.dumps([r.to_dictionary(), r2.to_dictionary()]),
                file.read())

    def test_save_to_file_empty_list(self):
        """Test if empty list is given to be saved.
        """
        # Create an empty list
        list_of_objs = []
        # Save the empty list to a file
        filename = 'Rectangle.json'
        Rectangle.save_to_file(list_of_objs)
        # Read the saved file
        with open(filename, 'r') as my_file:
            saved_data = my_file.read()
        expected_data = '[]'  # Verify the saved data
        self.assertEqual(saved_data, expected_data)

    def test_save_to_file_none(self):
        # Save None to a file
        filename = 'Rectangle.json'
        Rectangle.save_to_file(None)
        # Read the saved file
        with open(filename, 'r') as my_file:
            saved_data = my_file.read()
        # Verify the saved data
        expected_data = '[]'
        self.assertEqual(saved_data, expected_data)


if __name__ == '__main__':
    unittest.main()
