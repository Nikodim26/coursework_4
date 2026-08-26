import os

from src.receipt_by_criterion import ReceiptByCriterion
from src.utils import obtaining_information_on_the_criteria
from src.utils import translate_text


def test_obtaining_information_on_the_criteria(fixture_get_by_criterion) -> None:
    receipt_by_criterion = ReceiptByCriterion("1.json", [])
    assert obtaining_information_on_the_criteria("1.json",fixture_get_by_criterion) == [
        {"Altitude": 12146.28, "Country": "France", "ICAO24": "39de41", "Velocity": 236.75},
        {"Altitude": 388.62, "Country": "Germany", "ICAO24": "3d23da", "Velocity": 72.7},
    ]
    os.remove(receipt_by_criterion.path)


def test_translate_text() -> None:
    assert translate_text("германия") == "Germany"
    assert translate_text("germany") == "Germany"
