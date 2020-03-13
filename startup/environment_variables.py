import dotenv
import pathlib


def init():
    dotenv_path = pathlib.Path('.') / '.env'
    dotenv.load_dotenv(dotenv_path=dotenv_path)
