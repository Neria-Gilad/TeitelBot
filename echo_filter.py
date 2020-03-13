from util.punctuation_cleaner import cleanPunctuation

# TODO split into files and clean up this file


def having(bot, update):
    msg = update.effective_message.text
    words = cleanPunctuation(msg).split()
    idx = 0

    update.effective_message.reply_text('after clean punc '+' '.join(words))

    for w in words:
        if w == u"יש" or w == u"אין":
            break
        else:
            idx = idx + 1

    if idx == len(words):
        return False

    update.effective_message.reply_text('found domething to reverse')

    words = words[idx:]

    for i in enumerate(words):
        if words[i] == u"אין":
            words[i] = u"יש"
        elif words[i] == u"יש":
            words[i] = u"אין"
        elif words[i] == u"לי":
            words[i] = u"לך"
        elif words[i] == u"לך":
            words[i] = u"לי"

    update.effective_message.reply_text('done reversing')
    update.effective_message.reply_text(' '.join(words))
    return True


filter_list = [having]


def default_action(bot, update):
    update.effective_message.reply_text(update.effective_message.text + "v1")


def echo_filter(bot, update):
    for filter in filter_list:
        if filter(bot, update):
            return
    default_action(bot, update)
