from . import witai, dumb

language_processors = [witai, dumb]


class LanguageProcessor:
    @staticmethod
    def respond(message_raw_text):
        processor = language_processors[0]
        return processor.respond(message_raw_text)
