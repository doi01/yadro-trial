from typing import List, Dict, Any

class DeltaModel:
    """Модель для хранения дельта-изменений."""

    def __init__(self) -> None:
        """
        Инициализирует модель дельта-изменений с пустыми списками для добавлений, удалений и обновлений.
        """
        self.additions: List[Dict[str, Any]] = []
        self.deletions: List[Dict[str, Any]] = []
        self.updates: List[Dict[str, Any]] = []