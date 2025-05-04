import xml.etree.ElementTree as ET
from typing import List
from src.model.uml_model import UMLModel
from src.utils.logging_setup import get_logger

# Настройка логгера
logger = get_logger(__name__)

class XMLParser:
    """Парсер для обработки XML-файлов UML-модели."""

    def __init__(self, file_path: str) -> None:
        """
        Args:
            file_path (str): Путь к XML-файлу.
        """
        self.file_path = file_path
        self.models: List[UMLModel] = []

    def parse(self) -> None:
        """Парсит XML-файл и создает UML-модели."""
        try:
            logger.info(f"Начат парсинг XML-файла: {self.file_path}")
            tree = ET.parse(self.file_path)
            root = tree.getroot()

            for class_element in root.findall("Class"):
                model = self._parse_class(class_element)
                self.models.append(model)

            for aggregation_element in root.findall("Aggregation"):
                self._parse_aggregation(aggregation_element)

            logger.info(f"Парсинг XML-файла {self.file_path} завершен успешно.")
        except FileNotFoundError:
            logger.error(f"Файл {self.file_path} не найден.")
            raise
        except ET.ParseError as e:
            logger.error(f"Ошибка при парсинге XML-файла {self.file_path}: {e}")
            raise
        except Exception as e:
            logger.error(f"Неизвестная ошибка при парсинге XML-файла {self.file_path}: {e}")
            raise

    def _parse_class(self, element: ET.Element) -> UMLModel:
        """Парсит XML-элемент класса."""
        try:
            model = UMLModel(element.get("name"))
            model.documentation = element.get("documentation", "")
            model.isRoot = element.get("isRoot", "false").lower() == "true"

            for attr in element.findall("Attribute"):
                model.add_attribute(attr.get("name"), attr.get("type"))

            logger.debug(f"Класс {model.name} успешно распарсен.")
            return model
        except Exception as e:
            logger.error(f"Ошибка при парсинге класса: {e}")
            raise

    def _parse_aggregation(self, element: ET.Element) -> None:
        """Парсит XML-элемент агрегации."""
        try:
            source = element.get("source")
            target = element.get("target")

            if source and target:
                source_model = next((m for m in self.models if m.name == source), None)
                target_model = next((m for m in self.models if m.name == target), None)
                if source_model and target_model:
                    target_model.add_child(source_model)
                    logger.debug(f"Агрегация: {source} -> {target} успешно добавлена.")
        except Exception as e:
            logger.error(f"Ошибка при парсинге агрегации: {e}")
            raise

    def get_models(self) -> List[UMLModel]:
        """Возвращает список UML-моделей."""
        return self.models