import xml.etree.ElementTree as ET
from .model import Model

class Parser:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.models = {}

    def parse(self):
        tree = ET.parse(self.file_path)
        root = tree.getroot()
        for class_element in root.findall("Class"):
            model = self._parse_class(class_element)
            self.models[model.name] = model

        for aggregation_element in root.findall("Aggregation"):
            self._parse_aggregation(aggregation_element)

    def _parse_class(self, element):
        model = Model(element.get("name"))
        for attr in element.findall("Attribute"):
            model.add_attribute(attr.get("name"), attr.get("type"))
        return model

    def _parse_aggregation(self, element):
        source = element.get("source")
        target = element.get("target")
        if source in self.models and target in self.models:
            source_model = self.models[source]
            target_model = self.models[target]
            target_model.add_child(source_model)

    def get_models(self):
        return list(self.models.values())
