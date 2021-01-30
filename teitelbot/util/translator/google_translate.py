import googletrans


class GoogleTranslate:
    def __init__(self):
        self._translator = googletrans.Translator()

    def translate(self, text, src, dest) -> str:
        try:
            return self._translator.translate(text, src=src, dest=dest).text
        except (KeyError, AttributeError, ValueError) as e:
            raise RuntimeError("google translate package is unstable. it might got broken again.", e)
