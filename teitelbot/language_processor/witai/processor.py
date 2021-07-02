from . import classifier
from .classifier import WitParsedMessage


def respond(text: str) -> str:
    parsed_message: WitParsedMessage = classifier.ask_wit(text)

    return "tested wit"

