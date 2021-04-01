from util.language_processor import LanguageProcessor


class Response:
    def __init__(self, message_raw_text: str):
        self.processed_text = LanguageProcessor.parse(message_raw_text)
