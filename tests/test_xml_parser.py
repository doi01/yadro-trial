import unittest
import os
from src.parsers.xml_parser import XMLParser
from src.model.uml_model import UMLModel

class TestXMLParser(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_input.xml"
        with open(self.test_file, "w") as file:
            file.write("""
            <BTS>
                <Class name="TestClass" documentation="Test doc" isRoot="true">
                    <Attribute name="attr1" type="string" />
                </Class>
            </BTS>
            """)

    def tearDown(self):
        os.remove(self.test_file)

    def test_parse(self):
        parser = XMLParser(self.test_file)
        parser.parse()
        models = parser.get_models()
        self.assertEqual(len(models), 1)
        self.assertEqual(models[0].name, "TestClass")
        self.assertEqual(models[0].attributes["attr1"], "string")

if __name__ == "__main__":
    unittest.main()