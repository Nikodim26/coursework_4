import pytest


@pytest.fixture
def fixture_for_write_file() -> list:
    return [
        ["484966", 1, "Kingdom of the Netherlands", 3, 4, 5, 6, 7, 8, 262.37, 10, 11, 12, 12092.94, 14, 15, 16],
        ["484966", 1, "Poland", 3, 4, 5, 6, 7, 8, 162.37, 10, 11, 12, 10092.94, 14, 15, 16]
    ]
