import logging
from typing import Final

from response.exception import ResponseNotExistForAction, NoResponseException
from . import classifier
from .types import WitParsedMessage
from ..nlp_types import WeightedResponse, WeightedAction
from ..constants.action import Action

logger: Final = logging.getLogger(__name__)


def respond(text: str) -> WeightedResponse:
    parsed_message: WitParsedMessage = classifier.ask_wit(text)
    possible_actions: list[WeightedAction] = classifier.possible_actions(parsed_message)
    # todo: sort actions by confidence?
    for weighted_action in possible_actions:
        try:
            return get_response(weighted_action, parsed_message)
        except ResponseNotExistForAction as e:
            logger.error(e)
        except NoResponseException as e:
            logger.info(e)

    return WeightedResponse(None, 0)


def get_response(weighted_action: WeightedAction, parsed_message: WitParsedMessage) -> WeightedResponse:
    responses = {
        Action.EMAIL_ACTION: _email_response,
        Action.HAVING_ACTION: _having_response,
        Action.GENERIC_QUESTION_ACTION: _pointless_question_response,
    }

    try:
        return responses[weighted_action.action](parsed_message)
    except KeyError:
        raise ResponseNotExistForAction(weighted_action.action)


def _having_response(parsed_message: WitParsedMessage) -> WeightedResponse:
    ...


def _email_response(parsed_message: WitParsedMessage) -> WeightedResponse:
    ...


def _pointless_question_response(parsed_message: WitParsedMessage) -> WeightedResponse:
    ...
