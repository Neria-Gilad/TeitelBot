from wit_language_processor import WitLanguageProcessor
from dumb_language_processor import DumbLanguageProcessor

language_processors = {
    'None': DumbLanguageProcessor,
    'Wit': WitLanguageProcessor}


class NlpFactory:
    def __init__(self, chosen_processor: str = 'None'):
        self.processor = language_processors[chosen_processor]
