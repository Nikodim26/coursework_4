import json
import logging
from pathlib import Path

from working_with_files import Working_With_Files

logger = logging.getLogger(__name__)


class Receipt_by_Criterion(Working_With_Files):

    def __init__(self, file: str, data: list = None) -> None:
        super().__init__(file, data)
        self.path = Path(__file__).resolve().parent.parent / "data" / file

    def get_by_criterion(self, criterion) -> list:
        """Получает информацию о самолете по критерию"""

        try:
            with open(self.path, "r", encoding="utf-8") as f:
                data = json.load(f)

                result = data if criterion[0] == "All" else [dt for dt in data if dt["Country"] == criterion[0]]

                result = sorted(result, key=lambda x: x['Velocity'], reverse=True)

                if criterion[1] != 'All' and len(result) > int(criterion[1]):
                    result = sorted(result, key=lambda x: x['Velocity'], reverse=True)[:int(criterion[1])]

                if criterion[2] != "All":
                    result = [dt for dt in result if dt["Altitude"] <= int(criterion[2])]

            return result

        except Exception as e:
            logger.error(e)
            return []

    def write_file(self):
        pass

    def write_file_add(self, *args):
        pass
