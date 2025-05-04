import json
from typing import Any
from src.utils.logging_setup import get_logger

# Настройка логгера
logger = get_logger(__name__)

class JSONParser:
    """Парсер для обработки JSON-файлов."""

    def __init__(self, file_path: str) -> None:
        """
        Args:
            file_path (str): Путь к JSON-файлу.
        """
        self.file_path = file_path
        self.data: Any = {}

    def parse(self) -> None:
        """Парсит JSON-файл."""
        try:
            with open(self.file_path, "r") as file:
                self.data = json.load(file)
                logger.info(f"JSON-файл {self.file_path} успешно распарсен.")
        except FileNotFoundError:
            logger.error(f"Файл {self.file_path} не найден.")
            raise
        except json.JSONDecodeError as e:
            logger.error(f"Ошибка при парсинге JSON-файла {self.file_path}: {e}")
            raise
        except Exception as e:
            logger.error(f"Неизвестная ошибка при парсинге JSON-файла {self.file_path}: {e}")
            raise

    def get_data(self) -> Any:
        """Возвращает данные из JSON-файла."""
        return self.data