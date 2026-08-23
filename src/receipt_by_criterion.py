import json
import logging
from pathlib import Path

from working_with_files import Working_With_Files

logger = logging.getLogger(__name__)


class Receipt_by_Criterion(Working_With_Files):
    """Класс для объекта, извлекающего информацию по самолетам из файла согласно критериям поиска"""

    def __init__(self, file: str, data: list=None) -> None:
        super().__init__(file, data)
        self.path = Path(__file__).resolve().parent.parent / "data" / file

    def get_by_criterion(self, criteria: list) -> list:
        """Получает информацию о самолете по критерию"""

        try:
            with open(self.path, "r", encoding="utf-8") as f:
                data = json.load(f)

                result = data if criteria[0] == "All" else [dt for dt in data if dt["Country"] == criteria[0]]

                result = sorted(result, key=lambda x: x["Velocity"], reverse=True)

                if criteria[1] != "All" and len(result) > int(criteria[1]):
                    result = sorted(result, key=lambda x: x["Velocity"], reverse=True)[: int(criteria[1])]

                if criteria[2] != "All":
                    result = [
                        dt
                        for dt in result
                        if dt["Altitude"] <= int(criteria[2]) and dt["Velocity"] <= int(criteria[2])
                    ]

                return result

        except Exception as e:
            logger.error(e)
        return []

    def write_file(self) -> None:
        pass

    def write_file_add(self) -> None:
        pass
