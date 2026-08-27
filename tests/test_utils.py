import os
from pathlib import Path

from src.utils import translate_text
from src.utils import write_file


def test_translate_text() -> None:
    assert translate_text("германия") == "Germany"
    assert translate_text("germany") == "Germany"


def test_write_file(fixture_for_write_file) -> None:
    directory = Path(__file__).resolve().parent.parent / "data"

    before_the_entry = len([entry for entry in os.scandir(directory) if entry.is_file()])
    write_file("1.Json", fixture_for_write_file)
    after_recording = len([entry for entry in os.scandir(directory) if entry.is_file()])
    os.remove(Path(__file__).resolve().parent.parent / "data" / "1.Json")

    assert after_recording - before_the_entry == 1
