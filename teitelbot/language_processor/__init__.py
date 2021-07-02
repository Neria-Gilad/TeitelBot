import logging

from . import witai, dumb
from .parsed_message import ParsedResponse

language_processors = [witai, dumb]

LOGGER = logging.getLogger(__name__)


class LanguageProcessor:
    @staticmethod
    def respond(message_raw_text: str) -> str:
        for processor in language_processors:
            response: ParsedResponse = processor.respond(message_raw_text)
            if 0.8 < response.confidence:
                return response.text

        LOGGER.critical(f"No processor could handle the message: {message_raw_text}")
        return "שיט"
