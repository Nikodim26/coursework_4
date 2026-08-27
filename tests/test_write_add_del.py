import json
import os

from src.airplane import Airplane
from src.utils import write_file
from src.write_add_del import WriteAddDel

write_add_del = WriteAddDel("1.json")


def test_create_object() -> None:
    assert str(write_add_del.path_file)[-12:] == "\\data\\1.json"


def test_write_file(fixture_for_write_file) -> None:
    write_file("1.Json", fixture_for_write_file)
    assert write_add_del.reading_by_criteria(["Poland", "All", "All", "All"]) == [
        {"Altitude": 10092.94, "Country": "Poland", "ICAO24": "484966", "Velocity": 162.37}
    ]
    os.remove(write_add_del.path_file)


def test_write_file_add(capsys, fixture_for_write_file) -> None:
    write_file("1.Json", fixture_for_write_file)
    airplane = Airplane("a", "b", 1, 2)

    write_add_del.write_file_add(airplane)

    captured = capsys.readouterr()

    assert captured.out.strip() == "Добавлена информация о самолетах в файл\n\nДобавлена информация о новом самолете"
    os.remove(write_add_del.path_file)


def test_remove_from_file(fixture_for_write_file) -> None:
    write_file("1.Json", fixture_for_write_file)
    write_add_del.remove_from_file(["Poland"])

    with open(write_add_del.path_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert data == [
        {"Altitude": 12092.94, "Country": "Kingdom of the Netherlands", "ICAO24": "484966", "Velocity": 262.37}
    ]
    os.remove(write_add_del.path_file)
