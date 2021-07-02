from string import punctuation


def clean_punctuation(string: str) -> str:
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
        raise ValueError("substrings not found")

    return min_index


def replace_words(words: list, replacement_map: dict) -> list:
    return [
        word if word not in replacement_map.keys() else replacement_map[word]
        for word in words
    ]


def is_true(string: str) -> bool:
    return string and (string.lower() in ["true", "1", "t", "y", "yes", "yeah"])
