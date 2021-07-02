import logging

from response.exception import ResponseNotExistForAction, NoResponseException
from . import classifier
from .classifier import WitParsedMessage
from ..parsed_response import ParsedResponse
from ..constants.action import Action

LOGGER = logging.getLogger(__name__)


def respond(text: str) -> ParsedResponse:
    parsed_message: WitParsedMessage = classifier.ask_wit(text)
    if -1 == parsed_message.confidence:
        return ParsedResponse("", -1)
    try:
        return ParsedResponse(get_response(parsed_message.action, text), parsed_message.confidence)
    except ResponseNotExistForAction as e:
        LOGGER.error(e)
    except NoResponseException as e:
        LOGGER.info(e)

    return ParsedResponse("", -1)


def get_response(action: Action, text: str) -> str:
    responses = {
        Action.EMAIL_ACTION: _email_response,
        Action.HAVING_ACTION: _having_response,
        Action.GENERIC_QUESTION_ACTION: _pointless_question_response,
    }

    try:
        return responses[action](text)
    except KeyError:
        raise ResponseNotExistForAction(action)


def _having_response(text: str) -> str:
    ...


def _email_response(text: str) -> str:
    ...


def _pointless_question_response(text: str) -> str:
    ...
