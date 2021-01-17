import re
from random import random
from typing import List

import config
from constants.significant_words import words_to_repeat_sarcastically
from response.action import Action
from util import string_utils


def possible_actions(text: str) -> List[Action]:
    classifier_to_action = {
        _check_number: Action.CHECK_NUMBER_ACTION,
        _email: Action.EMAIL_ACTION,
        _having: Action.HAVING_ACTION,
        _generic_question: Action.GENERIC_QUESTION_ACTION,
        _repeat_sarcastically: Action.REPEAT_SARCASTICALLY_ACTION,
        _are_you_sure: Action.ARE_YOU_SURE_ACTION,
        _default: Action.DEFAULT_ACTION,
    }

    return [action for (classifier, action) in classifier_to_action.items() if classifier(text)] or [Action.NONE]


def _email(text: str):
    msg = string_utils.clean_punctuation(text)
    if 'מייל של ' not in msg:
        return False

    full_name = msg.split("מייל של ")[-1]
    return len(full_name.split()) <= 4


def _having(text: str):
    return any(word in ['יש', 'אין'] for word in text.split())


def _repeat_sarcastically(text: str):
    return bool(set(text.split()) & set(words_to_repeat_sarcastically))


def _default(_: str):
    return random() <= config.CHANCE_OF_RANDOM_RESPONSE


def _generic_question(text: str):
    return "?" in text and random() <= config.CHANCE_OF_RANDOM_RESPONSE


def _are_you_sure(text: str):
    return "בטוח?" in text


def _check_number(text: str) -> bool:
    is_number_regex = r'(?:(?:0)|(?:\+972))\d{8,9}'
    return bool(re.search(is_number_regex, text))
