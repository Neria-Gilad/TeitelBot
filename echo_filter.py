from random import random

from util.generic_response_generator import generic_negative_response, generic_answer
from util.string_utils import punctuation_cleaner, first_index_of_any
from echo_functions import having_action
import config


def default_action(bot, update):
    if random() <= config.CHANCE_OF_RANDOM_RESPONSE:
        update.effective_message.reply_text(generic_negative_response())


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


def generic_question(bot, update) -> bool:
    if "?" in update.effective_message.text:
        if random() <= config.CHANCE_OF_RANDOM_RESPONSE:
            update.effective_message.reply_text(generic_answer())
            return True
    return False


# add any filter to this list.
# filters always receive bot,update as arguments
# filters must either return False, or finish the job and return true
# they can send to another filter and return what that filter returned
filter_list = [
    having_filter,
    generic_question,
]


# just calls all the filters
def echo_filter(bot, update):
    for filter_func in filter_list:
        if filter_func(bot, update):
            break
    else:
        default_action(bot, update)
