import pytest

from src.airplane import Airplane


def test_create_object() -> None:
    airplane = Airplane("a", "b", 1, 2)
    assert airplane.ICAO24 == "a"
    assert airplane.Country_of_registration == "b"
    assert airplane.velocity == 1
    assert airplane.geo_altitude == 2
    del airplane


@pytest.mark.parametrize(
    "data", [["a", "b", -10, 20], ["a", "b", 10, -20], [None, "b", 10, 20], ["a", None, 10, 20], ["a", "b", 0, 20]]
)
def test_create_object_err(data) -> None:
    with pytest.raises(ValueError):
        Airplane(*data)


def test_comparison() -> None:
    airplane1 = Airplane("a", "b", 1, 2)
    airplane2 = Airplane("a", "b", 2, 3)
    assert airplane2 > airplane1
    del airplane1
    del airplane2


def test_str(capsys) -> None:
    airplane = Airplane("a", "b", 1, 2)
    print(airplane)
    captured = capsys.readouterr()
    assert captured.out.strip() == (
        "{\n" '    "ICAO24": "a",\n' '    "Country": "b",\n' '    "Velocity": 1,\n' '    "Altitude": 2\n' "}"
    )
    del airplane
