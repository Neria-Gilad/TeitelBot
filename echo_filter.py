

filter_list = []


def default_action(bot, update):
    update.effective_message.reply_text(update.effective_message.text)


def echo_filter(bot, update):
    for filter in filter_list:
        if filter(bot, update):
            return
    default_action(bot, update)
