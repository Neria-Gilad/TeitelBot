from util.string_utils import clean_punctuation
from util.translator import Translator

_translator = Translator()


def generate(full_name_in_hebrew: str) -> str:
    name = _get_translated_name(full_name_in_hebrew)
    suffix = "@g.jct.ac.il"

    return name + suffix


def _get_translated_name(name: str) -> str:
    translated_name = _translator.translate(name, src="he", dest="en").lower()
    return clean_punctuation(translated_name.replace(" ", ""))
