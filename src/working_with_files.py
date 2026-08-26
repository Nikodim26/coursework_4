from abc import ABC
from abc import abstractmethod
from pathlib import Path


class WorkingWithFiles(ABC):
    """Шаблон для объектов работающих с данными из файла, характеризующими самолеты"""

    def __init__(self, file: str, criteria: list) -> None:
        self.criteria = criteria
        self.path_file = Path(__file__).resolve().parent.parent / "data" / file

    @abstractmethod
    def reading_by_criteria(self) -> None:
        pass

    @abstractmethod
    def write_file_add(self) -> None:
        pass

    @abstractmethod
    def remove_from_file(self) -> None:
        pass
