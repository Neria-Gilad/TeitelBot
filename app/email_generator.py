import string

import googletrans


translator = googletrans.Translator()


def clean_punctuation(str):
    for punctuation in string.punctuation:
        str = str.replace(punctuation, "")
    return str


def get_translated_name(name: string):
    raw = translator.translate(name, src='iw', dest='en').text
    cleaned = clean_punctuation(raw.lower().replace(' ', ''))
    return cleaned


def generate(name: string):
    translated_name = get_translated_name(name)
    surfix = '@g.jct.ac.il'

    return translated_name + surfix
