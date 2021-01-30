from .google_translate import GoogleTranslate
from .ibm_watson_translator import IbmWatsonTranslator


class MultiProviderTranslator:
    def __init__(self, variant: str = 'both'):
        if variant in ['both', 'google']:
            self._translator = GoogleTranslate()
        elif variant == 'watson':
            self._translator = IbmWatsonTranslator()
        else:
            raise ValueError("variant must be set to 'both', 'google' or 'watson'")
        self._second_translator = IbmWatsonTranslator() if variant == 'both' else None

    def translate(self, text: str, src: str, dest: str) -> str:
        if not self._second_translator:
            return self._translator.translate(text, src, dest)

        try:
            return self._translator.translate(text, src, dest)
        except RuntimeError:
            return self._second_translator.translate(text, src, dest)
