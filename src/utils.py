import json
from pathlib import Path
from typing import Any

from translate import Translator

from src.airplane import Airplane
from src.api_airplanes import ApiAeroplanes


def translate_text(text: str) -> Any:
    """Переводит текст"""

    translator_to_en = Translator(to_lang="en")

    if "а" <= text[0] <= "я" or "А" <= text[0] <= "Я":
        return translator_to_en.translate(text).title()
    return text.title()


def write_file(file: str, api_airplanes: ApiAeroplanes) -> None:
    """Производит запись о самолетах в файл"""

    path_file = Path(__file__).resolve().parent.parent / "data" / file
    aeroplanes_list = []

    for dt in api_airplanes.list_info:
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
        except Exception:
            print("Не добавлена информация о самолетах в файл")

    if aeroplanes_list:
        with open(path_file, "w", encoding="utf-8") as f:
            json.dump(aeroplanes_list, f, indent=4, ensure_ascii=False)

        print("Добавлена информация о самолетах в файл\n")


def obtaining_information_on_the_criteria(path_file: Path, criteria: list) -> list:
    """Получает информацию о самолете по критериям"""

    try:
        with open(path_file, "r", encoding="utf-8") as f:
            data = json.load(f)

            result = data if criteria[0] == "All" else [dt for dt in data if dt["Country"] == criteria[0]]

            result = sorted(result, key=lambda x: x["Velocity"], reverse=True)

            if criteria[1] != "All" and len(result) > int(criteria[1]):
                result = sorted(result, key=lambda x: x["Velocity"], reverse=True)[: int(criteria[1])]

            if criteria[2] != "All":
                result = [
                    dt for dt in result if dt["Altitude"] <= int(criteria[2]) and dt["Velocity"] <= int(criteria[2])
                ]

            return result

    except Exception:
        print("Ошибка чтения файла данных")

    return []


def write_file_add(path_file: Path, airplane: Airplane) -> None:
    """Добавляет информацию о новом самолете в файл"""

    try:
        airplane_ = {
            "ICAO24": airplane.ICAO24,
            "Country": airplane.Country_of_registration,
            "Velocity": airplane.velocity,
            "Altitude": airplane.geo_altitude,
        }

        with open(path_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        if airplane_ not in data:
            data.append(airplane_)
        else:
            raise ValueError("Есть уже такой самолет")

        with open(path_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        print("Добавлена информация о новом самолете\n")

    except ValueError as e:
        print(e)

    except Exception as e:
        print(e)


def remove_from_file(path_file: Path, criteria: list) -> None:

    with open(path_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    data = [dt for dt in data if not dt["Country"] in criteria]

    with open(path_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
