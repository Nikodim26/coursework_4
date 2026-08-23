import json
import logging
from pathlib import Path

from adding_a_plane import Adding_Plane
from airplane import Airplane
from api_aeroplanes import Api_Aeroplanes
from api_coord import Api_Coord
from interpreter import translate_text
from receipt_by_criterion import Receipt_by_Criterion
from write_file import Write_File

log_path = Path(__file__).resolve().parent.parent / "logs" / "main.log"
logging.basicConfig(
    level=logging.INFO,
    filemode="w",
    encoding="UTF8",
    filename=log_path,
    datefmt="%d-%m-%Y в %H:%M:%S",
    format="%(levelname)s: %(asctime)s %(name)s %(message)s",
)
logger = logging.getLogger(__name__)


def working_with_the_user():
    """Предоставляет диалог с пользователем"""
    # while True:
    #     country = input('Укажите страну, в пространстве которой идет поиск самолетов: ')
    #     api_coord = Api_Coord(country)
    #     coordinates = api_coord.coordinates
    #     if coordinates:
    #         break
    #     print('Нет сведений')
    #
    #
    # print(coordinates)
    #
    # api_aeroplanes = Api_Aeroplanes(coordinates).list_info
    # print(api_aeroplanes)
    #
    # write_file = Write_File('aeroplanes.json', api_aeroplanes)
    # write_file.write_file()
    # logger.info(f'Добавлена информация о самолетах в файл')

    receipt_by_criterion = Receipt_by_Criterion('aeroplanes.json')
    # criterion = []
    # while True:
    #     country = input('Самолеты какой страны показать (все/страна)? [ВСЕ]: ')
    #     criterion.append(translate_text(country) if country != "" else 'All')
    #     quantity = input('Какое количество самых быстрых самолетов показать (все/N)? [ВСЕ]: ')
    #     criterion.append(quantity if quantity != "" else 'All')
    #     height = input('Укажите "потолок" (все/высота,м)? [ВСЕ]: ')
    #     criterion.append('All' if height == "" else height)
    #
    #     aeroplanes = receipt_by_criterion.get_by_criterion(criterion)
    #     if aeroplanes:
    #         print(json.dumps(aeroplanes, indent=4))
    #         break
    #     print('Нет сведений')

    # Выявление рекордсмена по высоте и скорости
    aeroplane_max = Airplane(" ", " ", 0, 0)
    aeroplanes_data = receipt_by_criterion.get_by_criterion(['All', 'All', 'All'])

    for dt in aeroplanes_data:
        aeroplane = Airplane(dt['ICAO24'],dt['Country'],dt['Velocity'],dt['Altitude'])
        if aeroplane > aeroplane_max:
            aeroplane_max = aeroplane

    print('Самый быстрый и высоколетящий самолет')
    print(json.dumps(aeroplane_max, indent=4))


if __name__ == '__main__':
    working_with_the_user()
