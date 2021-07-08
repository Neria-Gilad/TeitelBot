import logging
from typing import Final

from . import witai, dumb
from .nlp_types import WeightedResponse

language_processors = [witai, dumb]

logger: Final = logging.getLogger(__name__)


class LanguageProcessor:
    @staticmethod
    def respond(message_raw_text: str) -> str:
        for processor in language_processors:
            response: WeightedResponse = processor.respond(message_raw_text)
            if response.text is not None and response.confidence > 0.8:
                return response.text

        logger.critical(f"No processor could handle the message: {message_raw_text}")
        return "שיט"
