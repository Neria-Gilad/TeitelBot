from string import punctuation


def punctuation_cleaner(string: str):
    for p in punctuation:
        string = string.replace(p, "")
    return string


def first_index_of_any(lst, array_of_objects):
    min_index = len(lst) + 1  # out of index
    for obj in array_of_objects:
        try:
            min_index = min(min_index, lst.index(obj))
        except ValueError:
            pass
    if min_index == len(lst) + 1:
        raise ValueError('substrings not found')
    return min_index


def replace_words(word_list, replacement_map):
    return [
        word if word not in replacement_map.keys()
        else replacement_map[word]
        for word
        in word_list
    ]
