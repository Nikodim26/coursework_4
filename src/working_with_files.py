from abc import ABC
from abc import abstractmethod
from pathlib import Path

from src.airplane import Airplane


class WorkingWithFiles(ABC):
    """Шаблон для объектов работающих с данными из файла, характеризующими самолеты"""

    def __init__(self, file: str) -> None:
        self.path_file = Path(__file__).resolve().parent.parent / "data" / file

    @abstractmethod
    def reading_by_criteria(self, criteria: list) -> None:
        pass

    @abstractmethod
    def write_file_add(self, airplane: Airplane) -> None:
        pass

    @abstractmethod
    def remove_from_file(self, criteria: list) -> None:
        pass
