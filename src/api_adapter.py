from abc import ABC
from abc import abstractmethod


class APIAdapter(ABC):
    """Шаблон для классов, работающих с api"""

    def __init__(self) -> None:
        self.url = None

    @abstractmethod
    def obtaining_information(self) -> list | dict:
        """Получает информацию из api"""
        pass
