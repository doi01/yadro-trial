import json
from typing import Dict, Any, List
from src.utils.logging_setup import get_logger

# Настройка логгера
logger = get_logger(__name__)

class DeltaGenerator:
    """Генератор для создания delta.json."""

    def generate(self, config: Dict[str, Any], patched_config: Dict[str, Any]) -> Dict[str, List[Dict[str, Any]]]:
        """Генерирует дельта-изменения между исходным и патченным конфигами."""

        try:
            logger.info("Начата генерация дельта-изменений.")
            additions = []
            deletions = []
            updates = []

            for key, value in patched_config.items():
                if key not in config:
                    additions.append({"key": key, "value": value})
                elif config[key] != value:
                    updates.append({"key": key, "from": config[key], "to": value})

            for key in config:
                if key not in patched_config:
                    deletions.append({"key": key})

            delta = {
                "additions": additions,
                "deletions": deletions,
                "updates": updates
            }
            logger.info("Генерация дельта-изменений завершена успешно.")
            return delta
        except Exception as e:
            logger.error(f"Ошибка при генерации дельта-изменений: {e}")
            raise

    def save_to_file(self, delta: Dict[str, List[Dict[str, Any]]], file_path: str) -> None:
        """Сохраняет дельта-изменения в файл."""
        
        try:
            with open(file_path, "w") as file:
                json.dump(delta, file, indent=4)
            logger.info(f"Дельта-изменения успешно сохранены в файл {file_path}.")
        except Exception as e:
            logger.error(f"Ошибка при сохранении файла {file_path}: {e}")
            raise RuntimeError(f"Ошибка при сохранении файла {file_path}: {e}")