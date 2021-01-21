import logging
from random import choice
from typing import Callable, Any

import requests
from lxml import html

from constants.significant_words import words_to_repeat_sarcastically
from response import classifier
from response.action import Action
from response.exception import ResponseNotExistForAction, NoResponseException
from util import string_utils
from response.reply.service import email_generator, generic_response_generator

LOGGER = logging.getLogger(__name__)


def on_message(text: str, reply: Callable[[str], Any]) -> None:
    actions = classifier.possible_actions(text)
    for action in actions:
        try:
            response = get_response(action, text)
            reply(response)
            break
        except ResponseNotExistForAction as e:
            LOGGER.error(e)
        except NoResponseException as e:
            LOGGER.info(e)


def get_response(action: Action, text: str) -> str:
    if action == Action.CHECK_NUMBER_ACTION:
        return _identify_number_response(text)
    elif action == Action.EMAIL_ACTION:
        return _email_response(text)
    elif action == Action.HAVING_ACTION:
        return _having_response(text)
    elif action == Action.GENERIC_QUESTION_ACTION:
        return _generic_question_response()
    elif action == Action.REPEAT_SARCASTICALLY_ACTION:
        return _repeat_word_sarcastically_response(text)
    elif action == Action.DEFAULT_ACTION:
        return _default_response()

    raise ResponseNotExistForAction(action)


def _identify_number_response(text: str) -> str:
    no_result_text = "מבצע בדיקה ברחבי הרשת..."
    try:
        number_id_page = requests.get(f'https://call2me.co.il/{text}',
                                      verify=False,
                                      headers={'User-Agent': 'trust_me_bro'})
        result = html.fromstring(number_id_page.content).xpath("//div[contains(@class, 'resultData')]")
    except requests.RequestException as e:
        raise NoResponseException(f"error occurred while accessing call2me: {e}")
    except AttributeError:
        raise NoResponseException("error parsing html response")

    if not result:
        if "BLOCKED" in str(number_id_page.content):
            # keep DOS from denying us as well, let users know that they are annoying
            return "חפרת"
        raise NoResponseException("number not found")

    identified_number = result[0].text
    if identified_number != no_result_text:
        return identified_number
    raise NoResponseException("number not found")


def _default_response() -> str:
    return generic_response_generator.random_negative_response()


def _having_response(text: str) -> str:
    replaces_dict = {
        'אין': 'יש',
        'יש': 'אין',
        'לי': 'לך',
        'לך': 'לי',
    }
    words = string_utils.clean_punctuation(text).split()
    filtered_words = words[string_utils.first_index_of_any(words, ['יש', 'אין']):]

    return ' '.join(string_utils.replace_words(filtered_words, replaces_dict))


def _email_response(text: str) -> str:
    msg = string_utils.clean_punctuation(text)
    full_name = msg.split("מייל של ")[-1].strip()

    is_empty = not full_name or msg == "מייל של"
    return "של מי" if is_empty else email_generator.generate(full_name)


def _generic_question_response() -> str:
    return generic_response_generator.random_answer()


def _repeat_word_sarcastically_response(text: str) -> str:
    # for now (2021) sarcastically just means surround with quotes
    significant_words = list(set(text.split()) & set(words_to_repeat_sarcastically))
    return f'"{choice(significant_words)}"'
