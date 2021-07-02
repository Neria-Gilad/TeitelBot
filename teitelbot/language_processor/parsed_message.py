class ParsedMessage:
    def __init__(self, message_text: str, confidence: float):
        self.message_text = message_text
        self.confidence = confidence


class ParsedResponse:
    def __init__(self, response_text: str, confidence: float):
        self.text = response_text
        self.confidence = confidence
