import os
import pathlib

import dotenv


def add_dot_env_file_to_env():
    dotenv_path = pathlib.Path('.') / '.env'
    dotenv.load_dotenv(dotenv_path=dotenv_path)


add_dot_env_file_to_env()

NAME = 'TeitelBot'
TOKEN = os.environ.get('TOKEN')
PORT = os.environ.get('PORT')
IS_RUN_REMOTE = os.environ.get('IS_RUN_REMOTE')
CHANCE_OF_RANDOM_RESPONSE = 1.0
