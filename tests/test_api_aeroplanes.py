from unittest.mock import patch

from src.api_aeroplanes import Api_Aeroplanes


def test_create_object(fixture_coord) -> None:
    api_aeroplanes = Api_Aeroplanes(fixture_coord)
    assert api_aeroplanes.url == "https://opensky-network.org/api/states/all?"
    assert api_aeroplanes.coordinates == fixture_coord
    del api_aeroplanes

@patch('requests.get')
def test_obtaining_information(mock_get) -> None:
    api_aeroplanes = Api_Aeroplanes({})
    mock_get.return_value.json.return_value = {'states': ['aa9300', 'UAL47', 'United States', 178758, 178758]}
    mock_get.return_value.status_code = 200
    assert api_aeroplanes.obtaining_information() == ['aa9300', 'UAL47', 'United States', 178758, 178758]
    del api_aeroplanes

@patch('requests.get')
def test_obtaining_information_err(mock_get) -> None:
    api_aeroplanes = Api_Aeroplanes({})
    mock_get.return_value.json.return_value = {'states': ['aa9300', 'UAL47', 'United States', 178758, 178758]}
    mock_get.return_value.status_code = 400
    assert api_aeroplanes.obtaining_information() is None
    del api_aeroplanes