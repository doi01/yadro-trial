import xml.etree.ElementTree as ET
from xml.dom import minidom

class XMLGenerator:
    def __init__(self, root_model):
        self.root_model = root_model

    def _create_element(self, model):
        element = ET.Element(model.name)
        for attr in model.attributes:
            child = ET.SubElement(element, attr["name"])
            child.text = attr["type"]
        for child_model in model.children:
            element.append(self._create_element(child_model))
        return element

    def save_to_file(self, file_path):
        root_element = self._create_element(self.root_model)
        xml_str = ET.tostring(root_element, encoding="unicode")
        pretty_xml = minidom.parseString(xml_str).toprettyxml(indent="    ")
        with open(file_path, "w") as f:
            f.write(pretty_xml)
