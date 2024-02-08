#!/usr/bin/python3
"""Unittests for max_integer([..])."""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_int_and_float(self):
        """tests a list of both ints and floats."""
        floats_and_ints = [11.5, 6, 7.4, 0.2]
        self.assertEqual(max_integer(floats_and_ints), 11.5)

    def test_string(self):
        """Test a string"""
        string = "Hello"
        self.assertEqual(max_integer(string), 'o')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Esther", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [7, 8, 9, 10]
        self.assertEqual(max_integer(ordered), 10)

    def test_disordered_list(self):
        """Test a list that is not in ordered"""
        un_ordered = [8, 3, 12, 1]
        self.assertEqual(max_integer(un_ordered), 12)

    def test_max_at_beginning(self):
        """Test a list with maximum at the beginning"""
        list = [90, 4, 19, 20]
        self.assertEqual(max_integer(list), 90)

    def test_empty_list(self):
        """Test an empty list."""
        list = []
        self.assertEqual(max_integer(list), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        list = [9]
        self.assertEqual(max_integer(list), 9)

    def test_floats(self):
        """Test a list of floats."""
        list = [15.3, 7.33, 2.123, 19.2, 60.2]
        self.assertEqual(max_integer(list), 60.2)


if __name__ == '__main__':
    unittest.main()
