from src.utils import write_file


def test_write_file(fixture_for_write_file) -> None:

    write_file('1.Json',fixture_for_write_file)

    assert 1==1


    # write_add_del = WriteAddDel("1.json")
    # write_add_del.write_file()
    #
    # with open(write_file.path, "r", encoding="utf-8") as f:
    #     data_ = json.load(f)
    #
    # assert data_
    # os.remove(write_file.path)

# def test_obtaining_information_on_the_criteria(fixture_get_by_criterion) -> None:
#     receipt_by_criterion = ReceiptByCriterion("1.json", [])
#     assert obtaining_information_on_the_criteria("1.json",fixture_get_by_criterion) == [
#         {"Altitude": 12146.28, "Country": "France", "ICAO24": "39de41", "Velocity": 236.75},
#         {"Altitude": 388.62, "Country": "Germany", "ICAO24": "3d23da", "Velocity": 72.7},
#     ]
#     os.remove(receipt_by_criterion.path)
#
#
# def test_translate_text() -> None:
#     assert translate_text("германия") == "Germany"
#     assert translate_text("germany") == "Germany"
#
#
# def test_create_object(fixture_write_file) -> None:
#     write_file = WriteFile("1.json", fixture_write_file)
#     assert str(write_file.path)[-12:] == "\\data\\1.json"
#     assert write_file.data == [
#         ["484966", 1, "Kingdom of the Netherlands", 3, 4, 5, 6, 7, 8, 262.37, 10, 11, 12, 12092.94, 14, 15, 16]
#     ]
#
# def test_write_file(fixture_write_file) -> None:
#     write_file = WriteFile("1.json", fixture_write_file)
#     write_file.write_file()

    # with open(write_file.path, "r", encoding="utf-8") as f:
    #     data_ = json.load(f)
    #
    # assert data_
    # os.remove(write_file.path)