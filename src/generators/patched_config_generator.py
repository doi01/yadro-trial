import json
from typing import Dict, Any
from src.utils.logging_setup import get_logger

# Настройка логгера
logger = get_logger(__name__)

class PatchedConfigGenerator:
    """Генератор для создания res_patched_config.json."""

    def generate(self, config: Dict[str, Any], delta: Dict[str, Any]) -> Dict[str, Any]:
        """Генерирует патченный конфиг на основе исходного конфига и дельта-изменений."""

        try:
            logger.info("Начата генерация патченного конфига.")
            patched_config = config.copy()

            for addition in delta["additions"]:
                patched_config[addition["key"]] = addition["value"]
                logger.debug(f"Добавлено: {addition['key']} -> {addition['value']}")

            for deletion in delta["deletions"]:
                patched_config.pop(deletion["key"], None)
                logger.debug(f"Удалено: {deletion['key']}")

            for update in delta["updates"]:
                patched_config[update["key"]] = update["to"]
                logger.debug(f"Обновлено: {update['key']} -> {update['to']}")

            logger.info("Генерация патченного конфига завершена успешно.")
            return patched_config
        except Exception as e:
            logger.error(f"Ошибка при генерации патченного конфига: {e}")
            raise

    def save_to_file(self, patched_config: Dict[str, Any], file_path: str) -> None:
        """Сохраняет патченный конфиг в файл. """
        
        try:
            with open(file_path, "w") as file:
                json.dump(patched_config, file, indent=4)
            logger.info(f"Патченный конфиг успешно сохранен в файл {file_path}.")
        except Exception as e:
            logger.error(f"Ошибка при сохранении файла {file_path}: {e}")
            raise RuntimeError(f"Ошибка при сохранении файла {file_path}: {e}")