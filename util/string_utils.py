from string import punctuation

import googletrans

translator = googletrans.Translator()


def punctuation_cleaner(string: str) -> str:
    for p in punctuation:
        string = string.replace(p, "")
    return string


def first_index_of_any(lst: list, array_of_objects: list) -> int:
    min_index = len(lst) + 1  # out of index
    for obj in array_of_objects:
        try:
            min_index = min(min_index, lst.index(obj))
        except ValueError:
            pass
    if min_index == len(lst) + 1:
        raise ValueError('substrings not found')

    return min_index


def replace_words(words: list, replacement_map: dict) -> list:
    return [
        word if word not in replacement_map.keys()
        else replacement_map[word]
        for word
        in words
    ]


def translate_to_heb(string_in_english: str) -> str:
    return translator.translate(string_in_english, src='iw', dest='en').text
