from . import witai
from . import dumb

# language_processors = defaultdict(lambda: DumbLanguageProcessor)
# language_processors["Wit"] = WitLanguageProcessor

language_processors = {"Dumb": dumb, "Wit": witai}


class LanguageProcessor:
    def __init__(self):
        self.processor = language_processors["Dumb"]

    def respond(self, message_raw_text):
        return self.processor.respond(message_raw_text)
