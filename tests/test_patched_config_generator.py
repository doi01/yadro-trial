import unittest
from src.generators.patched_config_generator import PatchedConfigGenerator

class TestPatchedConfigGenerator(unittest.TestCase):
    def test_generate(self):
        config = {"key1": "value1", "key2": "value2"}
        delta = {
            "additions": [{"key": "key3", "value": "value3"}],
            "deletions": [{"key": "key2"}],
            "updates": [{"key": "key1", "to": "new_value1"}]
        }
        generator = PatchedConfigGenerator()
        patched_config = generator.generate(config, delta)
        self.assertEqual(patched_config["key1"], "new_value1")
        self.assertEqual(patched_config["key3"], "value3")
        self.assertNotIn("key2", patched_config)

if __name__ == "__main__":
    unittest.main()