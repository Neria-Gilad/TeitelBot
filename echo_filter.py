from random import random

from telegram import Update
from telegram.ext import CallbackContext

from util.generic_response_generator import generic_negative_response, generic_answer
from util.string_utils import punctuation_cleaner, first_index_of_any
from echo_functions import having_action, email_action
import config


def default_action(update: Update, context: CallbackContext):
    if random() <= config.CHANCE_OF_RANDOM_RESPONSE:
        update.message.reply_text(generic_negative_response())


# checks if the question is about (not) having something or something (not) existing
# answers a 'not true' statement based on the question
def having_filter(update: Update, context: CallbackContext) -> bool:
    msg = update.effective_message.text
    words = punctuation_cleaner(msg).split()

    try:
        index = first_index_of_any(words, ['יש', 'אין'])
    except ValueError:
        return False

    # the reply starts from where the *actual* question starts
    filtered_words = words[index:]

    having_action(filtered_words, update.message.reply_text)
    return True


def email_filter(update: Update, context: CallbackContext) -> bool:
    msg = update.effective_message.text
    msg = punctuation_cleaner(msg)
    if 'מייל של ' not in msg:
        return False

    full_name = msg.split("מייל של ")[-1]   # this makes it so just מייל של doesn't continue to email_action,
                                            # however, email_action has a check for מייל של. this is a bug
    is_too_long_name = len(full_name.split()) > 4
    if is_too_long_name:
        return False

    email_action(msg, full_name, update.message.reply_text)
    return True


def generic_question(update: Update, context: CallbackContext) -> bool:
    text = update.effective_message.text
    if "?" in text and random() <= config.CHANCE_OF_RANDOM_RESPONSE:
        update.message.reply_text(generic_answer())
        return True
    return False


# add any filter to this list.
# filters always receive bot,update as arguments
# filters must either return False, or finish the job and return true
# they can send to another filter and return what that filter returned
filter_list = [
    email_filter,
    having_filter,
    generic_question,
]


# just calls all the filters
def echo_filter(update: Update, context: CallbackContext):
    for filter_func in filter_list:
        if filter_func(update, context):
            break
    else:
        default_action(update, context)
