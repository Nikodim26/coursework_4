from translate import Translator


def translate_text(text):
    """Переводит текст"""

    translator_to_en = Translator(to_lang='en')

    if 'а' <= text[0] <= 'я' or 'А' <= text[0] <= 'Я':
        return translator_to_en.translate(text).title()
    return text.title()