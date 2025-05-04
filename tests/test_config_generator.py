import unittest
from xml.etree.ElementTree import fromstring
from src.generators.config_generator import ConfigGenerator
from src.model.uml_model import UMLModel

class TestConfigGenerator(unittest.TestCase):
    def test_generate(self):
        model = UMLModel("TestClass")
        model.isRoot = True
        model.add_attribute("attr1", "string")
        generator = ConfigGenerator()
        xml_output = generator.generate([model])
        root = fromstring(xml_output)
        self.assertEqual(root[0].tag, "TestClass")
        self.assertEqual(root[0][0].tag, "attr1")
        self.assertEqual(root[0][0].text, "string")

if __name__ == "__main__":
    unittest.main()