

def sure_filter(bot, update):
    if (u"בטוח?" in update.effective_message.text.split()):
        msg = u"ככה הבנתי"
        update.effective_message.reply_text(msg)
        return True
    return False


# add any filter to this list.
# filters always recieve bot,update as arguments
# filters must either return False, or finish the job and return true
# they can send to another filter and return what that filter returned
filter_list = [
    sure_filter
]


def default_action(bot, update):
    msg = u'מה הכוונה?'
    update.effective_message.reply_text(msg)


# just calls all the filters
def reply_filter(bot, update):
    for filter_func in filter_list:
        if filter_func(bot, update):
            break
    else:
        default_action(bot, update)
