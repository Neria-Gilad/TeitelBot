class ParsedMessage(object):
    def __init__(self, message_text: str, confidence: float):
        self.message_text = message_text
        self.confidence = confidence
