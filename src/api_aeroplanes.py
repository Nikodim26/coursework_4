import logging
from typing import Any

import requests

from src.api_adapter import APIAdapter

logger = logging.getLogger(__name__)


class Api_Aeroplanes(APIAdapter):
    '''Класс объекта, отвечающего за получение информации о самолетах в заданном "квадрате"'''

    def __init__(self, coordinates: dict) -> None:
        super().__init__()
        self.coordinates = coordinates
        self.url = "https://opensky-network.org/api/states/all?"
        self.list_info = self.obtaining_information()

    def obtaining_information(self) -> Any:
        """Получение информации о самолетах в координатах страны"""

        try:
            for i in range(3):
                logger.info(f"Делаю запрос - {i + 1} попытка")
                response = requests.get(url=self.url, params=self.coordinates)
                if str(response.status_code)[0] == "2":
                    logger.info(f"Ответ получен: код {response.status_code}")
                    break

            return response.json()["states"]

        except Exception as e:
            logger.error(e)
            return []
