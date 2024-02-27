#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import pep8


class TestBase(unittest.TestCase):
    """TestBase class to test various functionalities of the Base class."""

    def test_id_generation(self):
        """Test if IDs are generated properly."""
        Base._Base__nb_objects = 0
        obj = Base()
        self.assertIsNotNone(id(obj))

    def test_instance_creation(self):
        """Test if Base instances are created correctly."""
        Base._Base__nb_objects = 0
        obj = Base()
        self.assertIsInstance(obj, Base)

    def test_default_id_assignment(self):
        """Test if default IDs are assigned correctly."""
        Base._Base__nb_objects = 0
        obj = Base()
        self.assertEqual(obj.id, 1)

    def test_to_json_string_consistency(self):
        """Test if to_json_string provides consistent results."""
        Base._Base__nb_objects = 0
        rect = Rectangle(10, 7, 2, 8)
        rect_dict = rect.to_dictionary()
        json_string = json.dumps([rect_dict])
        json_list_dict = rect.to_json_string([rect_dict])
        self.assertTrue(json_string == json_list_dict)

    def test_save_to_file(self):
        """Test if save_to_file stores data correctly."""
        Base._Base__nb_objects = 0
        rect1 = Rectangle(10, 7, 2, 8)
        rect2 = Rectangle(2, 4)
        rect1_dict = rect1.to_dictionary()
        rect2_dict = rect2.to_dictionary()
        expected_data = [rect1_dict, rect2_dict]
        Rectangle.save_to_file([rect1, rect2])
        with open("Rectangle.json", "r") as file:
            stored_data = json.loads(file.read())
        self.assertTrue(expected_data == stored_data)

    def test_from_json_string(self):
        """Test if from_json_string provides correct data."""
        Base._Base__nb_objects = 0
        input_list = [{'id': 89, 'width': 10, 'height': 4},
                      {'id': 7, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(input_list)
        output_list = Rectangle.from_json_string(json_list_input)
        self.assertTrue(input_list == output_list)

    def test_create_method(self):
        """Test if the create method recreates objects correctly."""
        Base._Base__nb_objects = 0
        rect1 = Rectangle(3, 5, 1)
        rect1_dict = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dict)
        self.assertFalse(rect1 is rect2)
        self.assertFalse(rect1 == rect2)

    def test_load_from_file(self):
        """Test if load_from_file loads data correctly."""
        Base._Base__nb_objects = 0
        rect1 = Rectangle(10, 7, 2, 8)
        rect2 = Rectangle(2, 4)
        rect_input_list = [rect1, rect2]
        Rectangle.save_to_file(rect_input_list)
        rect_output_list = Rectangle.load_from_file()
        self.assertTrue(type(rect_output_list) == list)
        for rect in rect_input_list + rect_output_list:
            self.assertTrue(isinstance(rect, Rectangle))
        sqr1 = Square(5)
        sqr2 = Square(7, 9, 1)
        sqr_input_list = [sqr1, sqr2]
        Square.save_to_file(sqr_input_list)
        sqr_output_list = Square.load_from_file()
        self.assertTrue(type(sqr_output_list) == list)
        for sqr in sqr_input_list + sqr_output_list:
            self.assertTrue(isinstance(sqr, Square))

    def test_pep8_model(self):
        """Test if the code follows pep8 style guide."""
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(['models/base.py'])
        self.assertEqual(p.total_errors, 0, "Fix pep8 in model files")

    def test_pep8_test(self):
        """Test if the test code follows pep8 style guide."""
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(['tests/test_base.py'])
        self.assertEqual(p.total_errors, 0, "Fix pep8 in test files")


if __name__ == "__main__":
    unittest.main()
