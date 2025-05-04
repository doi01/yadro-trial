import logging
import os

LOG_DIR = "data/logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Настройка логирования
LOG_FILE = os.path.join(LOG_DIR, "application.log")
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_logger(name: str) -> logging.Logger:
    """Возвращает настроенный логгер."""
    return logging.getLogger(name)