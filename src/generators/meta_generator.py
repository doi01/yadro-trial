import json
from typing import List, Dict, Any
from src.model.uml_model import UMLModel
from src.utils.logging_setup import get_logger

# Настройка логгера
logger = get_logger(__name__)

class MetaGenerator:
    """Генератор для создания meta.json."""

    def generate(self, models: List[UMLModel]) -> List[Dict[str, Any]]:
        """Генерирует мета-данные на основе UML-моделей."""

        try:
            logger.info("Начата генерация мета-данных.")
            meta = []
            for model in models:
                meta.append({
                    "class": model.name,
                    "documentation": model.documentation,
                    "isRoot": model.isRoot,
                    "parameters": [
                        {"name": attr_name, "type": attr_type}
                        for attr_name, attr_type in model.attributes.items()
                    ]
                })
            logger.info("Генерация мета-данных завершена успешно.")
            return meta
        except Exception as e:
            logger.error(f"Ошибка при генерации мета-данных: {e}")
            raise

    def save_to_file(self, meta: List[Dict[str, Any]], file_path: str) -> None:
        """Сохраняет мета-данные в файл."""
        
        try:
            with open(file_path, "w") as file:
                json.dump(meta, file, indent=4)
            logger.info(f"Мета-данные успешно сохранены в файл {file_path}.")
        except Exception as e:
            logger.error(f"Ошибка при сохранении файла {file_path}: {e}")
            raise RuntimeError(f"Ошибка при сохранении файла {file_path}: {e}")