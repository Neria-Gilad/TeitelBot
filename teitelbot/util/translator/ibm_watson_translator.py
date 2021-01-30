from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

import config


class IbmWatsonTranslator:

    def __init__(self):
        self._translator = LanguageTranslatorV3(
            version=config.Watson.Translator.VERSION,
            authenticator=IAMAuthenticator(config.Watson.Translator.API_KEY)
        )
        self._translator.set_service_url(config.Watson.Translator.SERVICE_URL)

    def translate(self, text: str, src: str, dest: str) -> str:
        json = self._translator.translate([text], source=src, target=dest).get_result().json()
        first_translation = json['translations'][0]
        translated_text = first_translation['translation']
        return translated_text
