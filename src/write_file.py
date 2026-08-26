import json
import logging
from pathlib import Path

from src.airplane import Airplane
from src.working_with_files import WorkingWithFiles

logger = logging.getLogger(__name__)


class WriteFile(WorkingWithFiles):
    """Класс для объекта, записывающего информацию о самолетах в файл"""

    def __init__(self, file: str, data: list) -> None:
        super().__init__(file, data)
        self.path = Path(__file__).resolve().parent.parent / "data" / file
        self.data = data

    def write_file(self) -> None:
        """Производит запись о самолетах в файл"""
        aeroplanes_list = []

        for dt in self.data:
            try:
                aeroplane = Airplane(dt[0], dt[2], dt[9], dt[13])

                aeroplanes_list.append(
                    {
                        "ICAO24": aeroplane.ICAO24,
                        "Country": aeroplane.Country_of_registration,
                        "Velocity": aeroplane.velocity,
                        "Altitude": aeroplane.geo_altitude,
                    }
                )
                with open(self.path, "w", encoding="utf-8") as f:
                    json.dump(aeroplanes_list, f, indent=4, ensure_ascii=False)

            except Exception as e:
                logger.error(e)

        logger.info('Создана запись данных самолетов в заданном "квадрате" в файл')

    def write_file_add(self) -> None:
        pass

    def remove_from_file(self) -> None:
        pass