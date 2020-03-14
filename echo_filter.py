from util.punctuation_cleaner import punctuation_cleaner
from echo_functions import having_action


def default_action(bot, update):
    update.effective_message.reply_text('אין לי מה להגיד על זה')


def first_index(lst, array_of_objects):
    min_index = len(lst) + 1  # out of index
    for obj in array_of_objects:
        try:
            min_index = min(min_index, lst.index(obj))
        except ValueError:
            pass
    if min_index == len(lst) + 1:
        raise ValueError('substrings not found')
    return min_index


# checks if the question is about (not) having something or something (not) existing
# answers a 'not true' statement based on the question
def having_filter(bot, update) -> bool:
    msg = update.effective_message.text
    words = punctuation_cleaner(msg).split()

    try:
        index = first_index(words, ['יש', 'אין'])
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
