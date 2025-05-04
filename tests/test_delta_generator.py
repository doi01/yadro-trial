import unittest
from src.generators.delta_generator import DeltaGenerator

class TestDeltaGenerator(unittest.TestCase):
    def test_generate(self):
        config = {"key1": "value1", "key2": "value2"}
        patched_config = {"key1": "value1", "key2": "new_value2", "key3": "value3"}
        generator = DeltaGenerator()
        delta = generator.generate(config, patched_config)
        self.assertEqual(len(delta["additions"]), 1)
        self.assertEqual(delta["additions"][0]["key"], "key3")
        self.assertEqual(len(delta["updates"]), 1)
        self.assertEqual(delta["updates"][0]["key"], "key2")
        self.assertEqual(delta["updates"][0]["to"], "new_value2")
        self.assertEqual(len(delta["deletions"]), 0)

if __name__ == "__main__":
    unittest.main()