from random import random  # TODO replace this with tb_random
from telegram import Update
from telegram.ext import CallbackContext
import requests
from lxml import html

from util.tb_random import tb_choice
from util.generic_response_generator import generic_negative_response, generic_answer
from util.string_utils import punctuation_cleaner, first_index_of_any
from constants.significant_words import words_to_repeat_sarcastically

from echo_functions import having_action, email_action, repeat_sarcastically_action
import config


def check_number(update: Update, context: CallbackContext):
    # optimization
    if update.effective_message.text[0] != '0' and update.effective_message.text[0] != '+':
        return False

    no_result_text = "מבצע בדיקה ברחבי הרשת..."
    # access 'api' and parse response
    try:
        number_id_page = requests.get('https://call2me.co.il/' + update.effective_message.text, verify=False, headers={'User-Agent':'trustmebro'})
        tree = html.fromstring(number_id_page.content)
    except (AttributeError, requests.RequestException):
        return False
    number_id_page.close()

    # find result for requested number
    result = tree.xpath("//div[contains(@class, 'resultData')]")
    if len(result) < 1:
        if "BLOCKED" in str(number_id_page.content):
            # keep DOS from denying us as well, so return False but still let users know that they are annoying
            update.message.reply_text("חפרת")
        return False

    # check if api has a record of requested number and return it
    result_text = result[0].text
    if result_text != no_result_text:
        update.message.reply_text(result_text)
        return True
    return False


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

    full_name = msg.split("מייל של ")[-1]

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


def repeat_word_sarcastically_filter(update: Update, context: CallbackContext) -> bool:
    """
    checks for significant keywords and repeats one of them sarcastically if found
    """
    words = update.effective_message.text.split()
    significant_words = list(set(words) & set(words_to_repeat_sarcastically))
    if significant_words:
        repeat_sarcastically_action(tb_choice(significant_words), update.message.reply_text)
        return True
    return False


# add any filter to this list.
# filters always receive bot,update as arguments
# filters must either return False, or finish the job and return true
# they can send to another filter and return what that filter returned
filter_list = [
    check_number,
    email_filter,
    having_filter,
    generic_question,
    repeat_word_sarcastically_filter,
]


# just calls all the filters
def echo_filter(update: Update, context: CallbackContext):
    for filter_func in filter_list:
        if filter_func(update, context):
            break
    else:
        default_action(update, context)
