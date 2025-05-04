from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString
from typing import List
from src.model.uml_model import UMLModel
from src.utils.logging_setup import get_logger

# Настройка логгера
logger = get_logger(__name__)

class ConfigGenerator:
    """Генератор для создания config.xml."""

    def generate(self, models: List[UMLModel]) -> str:
        """Генерирует XML-документ на основе UML-моделей."""

        try:
            logger.info("Начата генерация config.xml.")
            root = Element("BTS")

            for model in models:
                if model.isRoot:
                    self._add_model_to_xml(root, model)

            rough_string = tostring(root, encoding="unicode")
            parsed = parseString(rough_string)
            logger.info("Генерация config.xml завершена успешно.")
            return parsed.toprettyxml(indent="    ")
        except Exception as e:
            logger.error(f"Ошибка при генерации config.xml: {e}")
            raise

    def _add_model_to_xml(self, parent: Element, model: UMLModel) -> None:
        """Рекурсивно добавляет модель в XML."""
        
        try:
            element = SubElement(parent, model.name)
            for attr_name, attr_type in model.attributes.items():
                attr = SubElement(element, attr_name)
                attr.text = attr_type

            for child in model.children:
                self._add_model_to_xml(element, child)
        except Exception as e:
            logger.error(f"Ошибка при добавлении модели {model.name} в XML: {e}")
            raise