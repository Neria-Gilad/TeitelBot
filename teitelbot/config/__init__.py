from os import environ

from config.env import inject_dotent_to_env
from util import string_utils

inject_dotent_to_env()

APP_NAME = environ.get('APP_NAME', 'teitelbot')
TOKEN = environ.get('TOKEN')
PORT = int(environ.get('PORT', 3000))
IS_RUN_REMOTE = string_utils.is_true(environ.get('IS_RUN_REMOTE', 'false'))
CHANCE_OF_RANDOM_RESPONSE = float(environ.get('CHANCE_OF_RANDOM_RESPONSE', 1.0))


class Watson:
    class Translator:
        API_KEY = environ.get('WATSON_TRANSLATOR_API_KEY')
        SERVICE_URL = environ.get('WATSON_TRANSLATOR_SERVICE_URL',
                                  'https://api.eu-gb.language-translator.watson.cloud.ibm.com')
        VERSION = environ.get('WATSON_TRANSLATOR_VERSION', '2018-05-01')
