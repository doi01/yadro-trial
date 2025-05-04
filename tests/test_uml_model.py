import unittest
from src.model.uml_model import UMLModel

class TestUMLModel(unittest.TestCase):
    def test_add_attribute(self):
        model = UMLModel("TestModel")
        model.add_attribute("attr1", "string")
        self.assertEqual(model.attributes["attr1"], "string")

    def test_add_child(self):
        parent = UMLModel("Parent")
        child = UMLModel("Child")
        parent.add_child(child)
        self.assertIn(child, parent.children)

    def test_is_root(self):
        model = UMLModel("RootModel")
        model.isRoot = True
        self.assertTrue(model.isRoot)

if __name__ == "__main__":
    unittest.main()