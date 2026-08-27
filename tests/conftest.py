import json

import pytest


@pytest.fixture
def fixture_for_write_file() -> dict:

    return {"time": 1766142246, "states": [
        ["484966", 1, "Kingdom of the Netherlands", 3, 4, 5, 6, 7, 8, 262.37, 10, 11, 12, 12092.94, 14, 15, 16],
        ["484966", 1, "Poland", 3, 4, 5, 6, 7, 8, 162.37, 10, 11, 12, 10092.94, 14, 15, 16]
        ]
            }

# @pytest.fixture
# def fixture_coord() -> dict:
#     return {"lamax": "55.0991610", "lamin": "47.2701114", "lomax": "15.0419309", "lomin": "5.8663153"}
#
#
# @pytest.fixture
# def fixture_get_by_criterion() -> list:
#     receipt_by_criterion = ReceiptByCriterion("1.json", [])
#     data_ = [
#         {"ICAO24": "3d23da", "Country": "Germany", "Velocity": 72.7, "Altitude": 388.62},
#         {"ICAO24": "39de41", "Country": "France", "Velocity": 236.75, "Altitude": 12146.28},
#     ]
#
#     with open(receipt_by_criterion.path, "w", encoding="utf-8") as f:
#         json.dump(data_, f, indent=4, ensure_ascii=False)
#
#     return ["All", "All", "All", "All"]
