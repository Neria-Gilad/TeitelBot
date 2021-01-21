from util.string_utils import translate_heb_to_eng, clean_punctuation


def generate(full_name_in_hebrew: str) -> str:
    name = _get_translated_name(full_name_in_hebrew)
    suffix = '@g.jct.ac.il'

    return name + suffix


def _get_translated_name(name: str) -> str:
    translated_name = translate_heb_to_eng(name).lower()
    return clean_punctuation(translated_name.replace(' ', ''))
