import json
import os

from src.write_file import Write_File


def test_create_object(fixture_write_file) -> None:
    write_file = Write_File("1.json", fixture_write_file)
    assert str(write_file.path)[-12:] == "\\data\\1.json"
    assert write_file.data == [
        ["484966", 1, "Kingdom of the Netherlands", 3, 4, 5, 6, 7, 8, 262.37, 10, 11, 12, 12092.94, 14, 15, 16]
    ]


def test_write_file(fixture_write_file) -> None:
    write_file = Write_File("1.json", fixture_write_file)
    write_file.write_file()

    with open(write_file.path, "r", encoding="utf-8") as f:
        data_ = json.load(f)

    assert data_
    os.remove(write_file.path)
