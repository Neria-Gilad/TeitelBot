import googletrans
from util.string_utils import translate_to_heb, punctuation_cleaner


def get_translated_name(name: str) -> str:
    translated_name = translate_to_heb(name).lower()
    cleaned = punctuation_cleaner(translated_name.replace(' ', ''))
    return cleaned


def generate(full_name_in_hebrew: str) -> str:
    name = get_translated_name(full_name_in_hebrew)
    suffix = '@g.jct.ac.il'

    return name + suffix
