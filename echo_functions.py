def having_action(words, update):
    map_object_replace = {
        'אין': 'יש',
        'יש': 'אין',
        'לי': 'לך',
        'לך': 'לי',
    }

    replaced_words = [
        w if w not in map_object_replace.keys()
        else map_object_replace[w]
        for w
        in words
    ]

    text = ' '.join(replaced_words)

    update.effective_message.reply_text(text)
