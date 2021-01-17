import logging
from typing import Callable, Any

from response import classifier
from response.action import Action
from response.exception import ResponseNotExistForAction

LOGGER = logging.getLogger(__name__)


def on_message(text: str, reply: Callable[[str], Any]) -> None:
    actions = classifier.possible_actions(text)
    for action in actions:
        try:
            response = get_response(action)
            reply(response)
            break
        except ResponseNotExistForAction as e:
            LOGGER.error(e)


def get_response(action: Action) -> str:
    if action == Action.ARE_YOU_SURE_ACTION:
        return _sure_response()
    elif action == Action.DEFAULT_ACTION:
        return _default_response()

    raise ResponseNotExistForAction(action)


def _sure_response() -> str:
    return "ככה הבנתי"


def _default_response() -> str:
    return 'מה הכוונה?'
