from src.utils import obtaining_information_on_the_criteria, write_file
from src.working_with_files import WorkingWithFiles


class WriteAddDel(WorkingWithFiles):
    """Класс для объекта, оперирующего с данными в файле"""

    def __init__(self, file: str, args: list) -> None:
        super().__init__(file,args)


    def reading_by_criteria(self) -> None:
        obtaining_information_on_the_criteria(self.path_file, self.args)


    def write_file_add(self) -> None:

    def remove_from_file(self) -> None:
