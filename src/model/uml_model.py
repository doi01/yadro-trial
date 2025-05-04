from typing import List, Dict

class UMLModel:
    """Модель UML-класса."""

    def __init__(self, name: str) -> None:
        """Инициализирует UML-модель."""

        self.name: str = name
        self.documentation: str = ""
        self.isRoot: bool = False
        self.attributes: Dict[str, str] = {}
        self.children: List[UMLModel] = []

    def add_attribute(self, name: str, attr_type: str) -> None:
        """Добавляет атрибут в модель."""

        self.attributes[name] = attr_type

    def add_child(self, child: "UMLModel") -> None:
        """Добавляет дочерний элемент в модель."""
        
        self.children.append(child)