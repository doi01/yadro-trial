import unittest
import os
import json
from src.parsers.json_parser import JSONParser

class TestJSONParser(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_config.json"
        with open(self.test_file, "w") as file:
            json.dump({"key1": "value1", "key2": "value2"}, file)

    def tearDown(self):
        os.remove(self.test_file)

    def test_parse(self):
        parser = JSONParser(self.test_file)
        parser.parse()
        data = parser.get_data()
        self.assertEqual(data["key1"], "value1")
        self.assertEqual(data["key2"], "value2")

if __name__ == "__main__":
    unittest.main()