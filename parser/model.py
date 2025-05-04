from typing import List

class Model:
    def __init__(self, name: str):
        self.name = name
        self.attributes = []
        self.children: List[Model] = []

    def add_attribute(self, name: str, attr_type: str):
        self.attributes.append({"name": name, "type": attr_type})

    def add_child(self, child: "Model"):
        self.children.append(child)

    def __str__(self):
        return f"Model(name={self.name}, attributes={self.attributes}, children={self.children})"
