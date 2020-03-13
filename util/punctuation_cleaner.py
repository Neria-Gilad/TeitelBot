import string


def cleanPunctuation(str):
    for p in string.punctuation:
        str = str.replace(p, "")
    return str
