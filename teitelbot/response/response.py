import logging
from typing import Callable, Any, Final

from language_processor import LanguageProcessor
from response.exception import FailedToRespondException

logger: Final = logging.getLogger(__name__)


def _respond(message_raw_text: str):
    return LanguageProcessor().respond(message_raw_text)


def on_message(text: str, reply: Callable[[str], Any]) -> None:
    # todo: logic to limit responses in groups
    try:
        reply(_respond(text))
    except FailedToRespondException as e:
        logger.error(e)


def on_quote(text: str, reply: Callable[[str], Any]) -> None:
    try:
        reply(_respond(text))
    except FailedToRespondException as e:
        logger.error(e)
