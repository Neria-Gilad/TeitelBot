import logging
from collections import defaultdict
from random import choice
from typing import Callable, Any, Final

import requests
from lxml import html

from . import classifier
from language_processor.constants.significant_words import words_to_repeat_sarcastically
from language_processor.constants.action import Action
from response.exception import (
    ResponseNotExistForAction,
    NoResponseException,
    FailedToRespondException,
)
from util import string_utils
from ..nlp_types import WeightedResponse
from ..util import generic_response_generator, email_generator

logger: Final = logging.getLogger(__name__)


def respond(text: str) -> WeightedResponse:
    actions = classifier.possible_actions(text)
    for weighted_action in actions:
        try:
            return WeightedResponse(get_response(weighted_action.action, text), 1)
        except ResponseNotExistForAction as e:
            logger.error(e)
        except NoResponseException as e:
            logger.info(e)

    raise FailedToRespondException(text)


def get_response(action: Action, text: str) -> str:
    responses = {
        Action.CHECK_NUMBER_ACTION: _identify_number_response,
        Action.EMAIL_ACTION: _email_response,
        Action.HAVING_ACTION: _having_response,
        Action.ARE_YOU_SURE_ACTION: _assure_response,
        Action.GENERIC_QUESTION_ACTION: _generic_question_response,
        Action.REPEAT_SARCASTICALLY_ACTION: _identify_number_response,
        Action.DEFAULT_ACTION: _default_response,
    }

    try:
        return responses[action](text)
    except KeyError:
        raise ResponseNotExistForAction(action)


def _identify_number_response(text: str) -> str:
    no_result_text = "מבצע בדיקה ברחבי הרשת..."
    try:
        number_id_page = requests.get(
            f"https://call2me.co.il/{text}",
            verify=False,
            headers={"User-Agent": "trust_me_bro"},
        )
        result = html.fromstring(number_id_page.content).xpath(
            "//div[contains(@class, 'resultData')]"
        )
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


def _default_response(text: str) -> str:
    return generic_response_generator.random_negative_response()


def _having_response(text: str) -> str:
    replaces_dict = {
        "אין": "יש",
        "יש": "אין",
        "לי": "לך",
        "לך": "לי",
    }
    words = string_utils.clean_punctuation(text).split()
    filtered_words = words[string_utils.first_index_of_any(words, ["יש", "אין"]):]

    return " ".join(string_utils.replace_words(filtered_words, replaces_dict))


def _email_response(text: str) -> str:
    msg = string_utils.clean_punctuation(text)
    full_name = msg.split("מייל של ")[-1].strip()

    is_empty = not full_name or msg == "מייל של"
    return "של מי" if is_empty else email_generator.generate(full_name)


def _generic_question_response(text: str) -> str:
    return generic_response_generator.random_answer()


def _assure_response(text: str) -> str:
    return "ככה הבנתי"


def _repeat_word_sarcastically_response(text: str) -> str:
    # for now (2021) sarcastically just means surround with quotes
    significant_words = list(set(text.split()) & set(words_to_repeat_sarcastically))
    return f'"{choice(significant_words)}"'
