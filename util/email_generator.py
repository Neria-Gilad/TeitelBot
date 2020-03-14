import googletrans

from util.punctuation_cleaner import punctuation_cleaner

translator = googletrans.Translator()


def get_translated_name(name: str):
    raw = translator.translate(name, src='iw', dest='en').text
    cleaned = punctuation_cleaner(raw.lower().replace(' ', ''))
    return cleaned


def generate(full_name_in_hebrew: str):
    translated_name = get_translated_name(full_name_in_hebrew)
    suffix = '@g.jct.ac.il'

    return translated_name + suffix
