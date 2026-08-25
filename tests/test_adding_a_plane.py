import json

from src.adding_a_plane import AddingPlane


def test_write_file_add() -> None:
    adding_plane = AddingPlane("aeroplanes.json", [])
    path = adding_plane.path
    with open(path, "r", encoding="utf-8") as f:
        data_old = json.load(f)

    adding_plane.write_file_add(["abc", "Germany", 100, 1000])

    with open(path, "r", encoding="utf-8") as f:
        data_new = json.load(f)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data_old, f, indent=4, ensure_ascii=False)

    assert len(data_old) < len(data_new)
    del adding_plane
