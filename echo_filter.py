from util.punctuation_cleaner import cleanPunctuation
from echo_functions import *


def default_action(bot, update):
    update.effective_message.reply_text('אין לי מה להגיד על זה')


# checks if the question is about (not) having something or something (not) existing
# answers a 'not true' statement based on the question
def havingFilter(bot, update):
    msg = update.effective_message.text
    words = cleanPunctuation(msg).split()
    idx = 0

    for w in words:
        if w == u"יש" or w == u"אין":
            break
        else:
            idx = idx + 1

    if idx == len(words):
        return False

    # the reply starts from where the *actual* question starts
    words = words[idx:]

    havingAction(words, update)
    return True


# add any filter to this list.
# filters always recieve bot,update as arguments
# filters must either return False, or finish the job and return true
# they can send to another filter and return what that filter returned
filter_list = [
    havingFilter
]


# just calls all the filters
def echo_filter(bot, update):
    for filter in filter_list:
        if filter(bot, update):
            return
    default_action(bot, update)
