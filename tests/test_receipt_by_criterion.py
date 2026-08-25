import os

from src.receipt_by_criterion import Receipt_by_Criterion


def test_get_by_criterion(fixture_get_by_criterion) -> None:
    receipt_by_criterion = Receipt_by_Criterion('1.json', [])

    assert receipt_by_criterion.get_by_criterion(fixture_get_by_criterion) == [
        {'Altitude': 12146.28,
         'Country': 'France',
         'ICAO24': '39de41',
         'Velocity': 236.75},
        {'Altitude': 388.62,
         'Country': 'Germany',
         'ICAO24': '3d23da',
         'Velocity': 72.7}
    ]
    os.remove(receipt_by_criterion.path)
    del receipt_by_criterion