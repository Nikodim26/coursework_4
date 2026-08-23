from abc import ABC
from abc import abstractmethod


class Working_With_Files(ABC):
    """Шаблон для объектов работающих с данными из файла, характеризующими самолеты"""

    def __init__(self, file: str, data: list) -> None:
        self.file = file
        self.data = data

    @abstractmethod
    def write_file(self) -> None:
        pass

    @abstractmethod
    def write_file_add(self) -> None:
        pass

    @abstractmethod
    def get_by_criterion(self) -> None:
        pass
