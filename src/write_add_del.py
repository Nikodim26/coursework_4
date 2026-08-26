from typing import Any

from src.airplane import Airplane
from src.utils import obtaining_information_on_the_criteria
from src.utils import remove_from_file
from src.utils import write_file_add
from src.working_with_files import WorkingWithFiles


class WriteAddDel(WorkingWithFiles):
    """Класс для объекта, оперирующего с данными в файле"""

    def __init__(self, file: str) -> None:
        super().__init__(file)

    def reading_by_criteria(self, args: list) -> list:
        return obtaining_information_on_the_criteria(self.path_file, args)

    def write_file_add(self, args: Airplane) -> None:
        write_file_add(self.path_file, args)

    def remove_from_file(self, args: list) -> None:
        remove_from_file(self.path_file, args)
