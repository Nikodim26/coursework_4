from src.interpreter import translate_text


def test_translate_text() -> None:
    assert translate_text("германия") == "Germany"
    assert translate_text("germany") == "Germany"
