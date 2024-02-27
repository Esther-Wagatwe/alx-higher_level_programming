import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_auto_assign_id(self):
        obj1 = Base()
        obj2 = Base()
        obj3 = Base(id=10)

        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
        self.assertEqual(obj3.id, 10)

    def test_id_assignment(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj2.id, obj1.id + 1)

    def test_id_passed(self):
        obj = Base(89)
        self.assertEqual(obj.id, 89)

    def test_to_json_string_with_none(self):
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_to_json_string_with_empty_list(self):
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_returning_string(self):
        input_list = [{'id': 12}]
        result = Base.to_json_string(input_list)
        self.assertIsInstance(result, str)

    def test_from_json_string_exists(self):
        with self.assertRaises(AttributeError):
            Base.from_json_string(None)

    def test_from_json_string_exists(self):
        result = Base.from_json_string("[]")
        self.assertEqual(result, [])

    def test_from_json_string_with_data_exists(self):
        result = Base.from_json_string('[{ "id": 89 }]')
        self.assertEqual(result, [{"id": 89}])

    def test_from_json_string_returns_list(self):
        result = Base.from_json_string('[{ "id": 89 }]')
        self.assertIsInstance(result, list)


if __name__ == "__main__":
    unittest.main()
