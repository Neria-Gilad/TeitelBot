from . import classifier


def respond(text: str) -> str:
    wut = classifier.ask_wit(text)
    return "tested wit"

