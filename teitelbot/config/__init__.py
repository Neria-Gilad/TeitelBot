import os

from config.env import inject_dotent_to_env
from util import string_utils

inject_dotent_to_env()

APP_NAME = os.environ.get('APP_NAME', 'teitelbot')
TOKEN = os.environ.get('TOKEN')
PORT = int(os.environ.get('PORT', 3000))
IS_RUN_REMOTE = string_utils.is_true(os.environ.get('IS_RUN_REMOTE', 'false'))
CHANCE_OF_RANDOM_RESPONSE = float(os.environ.get('CHANCE_OF_RANDOM_RESPONSE', 1.0))
