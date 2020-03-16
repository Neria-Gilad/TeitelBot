from util.string_utils import punctuation_cleaner, first_index_of_any
from echo_functions import having_action


def default_action(bot, update):
    update.effective_message.reply_text('אין לי מה להגיד על זה')


# checks if the question is about (not) having something or something (not) existing
# answers a 'not true' statement based on the question
def having_filter(bot, update) -> bool:
    msg = update.effective_message.text
    words = punctuation_cleaner(msg).split()

    try:
        index = first_index_of_any(words, ['יש', 'אין'])
    except ValueError:
        return False

    # the reply starts from where the *actual* question starts
    filtered_words = words[index:]

    having_action(filtered_words, update)
    return True


# add any filter to this list.
# filters always recieve bot,update as arguments
# filters must either return False, or finish the job and return true
# they can send to another filter and return what that filter returned
filter_list = [
    having_filter
]


# just calls all the filters
def echo_filter(bot, update):
    for filter_func in filter_list:
        if filter_func(bot, update):
            break
    else:
        default_action(bot, update)
