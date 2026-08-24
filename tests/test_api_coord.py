from unittest.mock import patch

from src.api_coord import Api_Coord


def test_create_object() -> None:
    api_coord = Api_Coord('Germany')
    assert api_coord.country == 'Germany'
    assert api_coord.url == "https://nominatim.openstreetmap.org/search"
    assert api_coord.coordinates == {'lamax': '55.0991610',
                                     'lamin': '47.2701114',
                                     'lomax': '15.0419309',
                                     'lomin': '5.8663153'}


@patch('requests.get')
def test_obtaining_information(mock_get) -> None:
    api_coord = Api_Coord('Germany')
    mock_get.return_value.json.return_value = [{'boundingbox': ['1', '2', '3', '4']}]
    mock_get.return_value.status_code = 200
    assert api_coord.obtaining_information() == {"lamin": '1', "lamax": '2', "lomin": '3', "lomax": '4'}


@patch('requests.get')
def test_obtaining_information_err(mock_get) -> None:
    api_coord = Api_Coord('Germany')
    mock_get.return_value.json.return_value = [{'boundingbox': ['1', '2', '3', '4']}]
    mock_get.return_value.status_code = 400
    assert api_coord.obtaining_information() is None
