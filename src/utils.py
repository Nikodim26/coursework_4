import json
import logging
from typing import Any

from translate import Translator

logger = logging.getLogger(__name__)


def translate_text(text: str) -> Any:
    """Переводит текст"""

    translator_to_en = Translator(to_lang="en")

    if "а" <= text[0] <= "я" or "А" <= text[0] <= "Я":
        return translator_to_en.translate(text).title()
    return text.title()


def obtaining_information_on_the_criteria(self, criteria: list) -> list:
    """Получает информацию о самолете по критериям"""

    try:
        with open(self.path, "r", encoding="utf-8") as f:
            data = json.load(f)

            result = data if criteria[0] == "All" else [dt for dt in data if dt["Country"] == criteria[0]]

            result = sorted(result, key=lambda x: x["Velocity"], reverse=True)

            if criteria[1] != "All" and len(result) > int(criteria[1]):
                result = sorted(result, key=lambda x: x["Velocity"], reverse=True)[: int(criteria[1])]

            if criteria[2] != "All":
                result = [
                    dt
                    for dt in result
                    if dt["Altitude"] <= int(criteria[2]) and dt["Velocity"] <= int(criteria[2])
                ]

            return result

    except Exception as e:
        logger.error(e)
    return []
