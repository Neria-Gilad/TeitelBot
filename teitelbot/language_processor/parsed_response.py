class ParsedResponse:
    def __init__(self, response_text: str, confidence: float):
        self.text = response_text
        self.confidence = confidence
