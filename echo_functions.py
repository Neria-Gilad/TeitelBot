from util.string_utils import replace_words
from util.email_generator import generate


# responds with the opposite of the question in terms of (not) having something
def having_action(words, response):
    map_object_replace = {
        'אין': 'יש',
        'יש': 'אין',
        'לי': 'לך',
        'לך': 'לי',
    }

    replaced_words = replace_words(words, map_object_replace)
    text = ' '.join(replaced_words)

    response(text)


def email_action(raw_msg, name, response):
    is_empty = not name.strip() or raw_msg == "מייל של"
    text = "של מי" if is_empty else generate(name)

    response(text)
