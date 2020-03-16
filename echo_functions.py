from util.string_utils import replace_words


# responds with the opposite of the question in terms of (not) having something
def having_action(words, update):
    map_object_replace = {
        'אין': 'יש',
        'יש': 'אין',
        'לי': 'לך',
        'לך': 'לי',
    }

    replaced_words = replace_words(words, map_object_replace)
    text = ' '.join(replaced_words)

    update.effective_message.reply_text(text)
