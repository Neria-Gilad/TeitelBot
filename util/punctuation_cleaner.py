from string import punctuation


def punctuation_cleaner(string: str):
    for p in punctuation:
        string = string.replace(p, "")
    return string
