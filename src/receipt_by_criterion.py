import json
import logging
from pathlib import Path

from src.working_with_files import WorkingWithFiles

logger = logging.getLogger(__name__)


class ReceiptByCriterion(WorkingWithFiles):
    """Класс для объекта, извлекающего информацию по самолетам из файла согласно критериям поиска"""

    def __init__(self, file: str, data: list) -> None:
        super().__init__(file, data)
        self.path = Path(__file__).resolve().parent.parent / "data" / file



    def write_file(self) -> None:
        pass

    def write_file_add(self) -> None:
        pass
