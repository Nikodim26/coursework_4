import json
import logging
from pathlib import Path

from airplane import Airplane
from working_with_files import Working_With_Files

logger = logging.getLogger(__name__)


class Adding_Plane(Working_With_Files):
    """Класс для объекта, добавляющего информацию о новом самолете"""

    def __init__(self, file: str, data: list=None) -> None:
        super().__init__(file, data)
        self.path = Path(__file__).resolve().parent.parent / "data" / file

    def write_file_add(self, *args) -> None:
        """Добавляет информацию о новом самолете в файл"""

        try:
            new_aeroplane = Airplane(*args)
            aeroplane = {
                "ICAO24": new_aeroplane.ICAO24,
                "Country": new_aeroplane.Country_of_registration,
                "Velocity": new_aeroplane.velocity,
                "Altitude": new_aeroplane.geo_altitude
            }

            with open(self.path, "r", encoding="utf-8") as f:
                data = json.load(f)
            if not aeroplane in data:
                data.append(aeroplane)
            else:
                raise ValueError('Есть уже такой самолет')

            with open(self.path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)

            logger.info(f'Добавлена информация о новом самолете в файл')
        except ValueError as e:
            print(e)

        except Exception as e:
            logger.error(e)

    def write_file(self):
        pass

    def get_by_criterion(self,):
        pass