import json
import os
from src.parsers.xml_parser import XMLParser
from src.parsers.json_parser import JSONParser
from src.generators.config_generator import ConfigGenerator
from src.generators.meta_generator import MetaGenerator
from src.generators.delta_generator import DeltaGenerator
from src.generators.patched_config_generator import PatchedConfigGenerator
from src.utils.logging_setup import get_logger

# Настройка логгера
logger = get_logger(__name__)

def load_config(config_path: str) -> dict:
    """Загружает конфигурацию из JSON-файла."""
    try:
        with open(config_path, "r") as file:
            config = json.load(file)
            logger.info(f"Конфигурация загружена из {config_path}")
            return config
    except Exception as e:
        logger.error(f"Ошибка при загрузке конфигурации: {e}")
        raise

def main() -> None:
    try:
        logger.info("Программа запущена.")

        # Загрузка конфигурации
        config = load_config("config.json")
        input_dir = config["input_dir"]
        output_dir = config["output_dir"]

        # Убедимся, что выходная директория существует
        os.makedirs(output_dir, exist_ok=True)
        logger.info(f"Выходная директория: {output_dir}")

        # Парсинг XML
        xml_input_path = os.path.join(input_dir, config["xml_input_file"])
        xml_parser = XMLParser(xml_input_path)
        xml_parser.parse()
        models = xml_parser.get_models()
        logger.info(f"XML-файл {xml_input_path} успешно распарсен.")

        # Генерация config.xml
        config_gen = ConfigGenerator()
        config_xml = config_gen.generate(models)
        config_output_path = os.path.join(output_dir, config["config_output_file"])
        with open(config_output_path, "w") as file:
            file.write(config_xml)
        logger.info(f"Файл config.xml сохранен в {config_output_path}")

        # Генерация meta.json
        meta_gen = MetaGenerator()
        meta = meta_gen.generate(models)
        meta_output_path = os.path.join(output_dir, config["meta_output_file"])
        meta_gen.save_to_file(meta, meta_output_path)
        logger.info(f"Файл meta.json сохранен в {meta_output_path}")

        # Парсинг JSON
        json_config_path = os.path.join(input_dir, config["json_config_file"])
        json_parser = JSONParser(json_config_path)
        json_parser.parse()
        config_data = json_parser.get_data()
        logger.info(f"JSON-файл {json_config_path} успешно распарсен.")

        patched_json_config_path = os.path.join(input_dir, config["patched_json_config_file"])
        patched_json_parser = JSONParser(patched_json_config_path)
        patched_json_parser.parse()
        patched_config = patched_json_parser.get_data()
        logger.info(f"JSON-файл {patched_json_config_path} успешно распарсен.")

        # Генерация delta.json
        delta_gen = DeltaGenerator()
        delta = delta_gen.generate(config_data, patched_config)
        delta_output_path = os.path.join(output_dir, config["delta_output_file"])
        delta_gen.save_to_file(delta, delta_output_path)
        logger.info(f"Файл delta.json сохранен в {delta_output_path}")

        # Генерация res_patched_config.json
        patched_config_gen = PatchedConfigGenerator()
        patched_config_result = patched_config_gen.generate(config_data, delta)
        patched_config_output_path = os.path.join(output_dir, config["patched_config_output_file"])
        patched_config_gen.save_to_file(patched_config_result, patched_config_output_path)
        logger.info(f"Файл res_patched_config.json сохранен в {patched_config_output_path}")

        logger.info("Программа успешно завершена.")
    except Exception as e:
        logger.error(f"Ошибка в процессе выполнения программы: {e}")
        raise

if __name__ == "__main__":
    main()