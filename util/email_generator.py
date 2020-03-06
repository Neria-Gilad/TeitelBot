from string import punctuation

import googletrans

translator = googletrans.Translator()


def clean_punctuation(string: str):
    for p in punctuation:
        string = string.replace(p, "")
    return string


def get_translated_name(name: str):
    raw = translator.translate(name, src='iw', dest='en').text
    cleaned = clean_punctuation(raw.lower().replace(' ', ''))
    return cleaned


def generate(full_name_in_hebrew: str):
    translated_name = get_translated_name(full_name_in_hebrew)
    suffix = '@g.jct.ac.il'

    return translated_name + suffix
