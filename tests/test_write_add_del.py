from src.write_add_del import WriteAddDel


def test_create_object() -> None:
    write_add_del = WriteAddDel("1.json")
    assert str(write_add_del.path_file)[-12:] == "\\data\\1.json"


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
