def havingAction(words, update):
    for i, _ in enumerate(words):
        if words[i] == u"אין":
            words[i] = u"יש"
        elif words[i] == u"יש":
            words[i] = u"אין"
        elif words[i] == u"לי":
            words[i] = u"לך"
        elif words[i] == u"לך":
            words[i] = u"לי"

    update.effective_message.reply_text(' '.join(words))
