import pathlib

import dotenv


def inject_dotent_to_env():
    dotenv.load_dotenv(dotenv_path=(pathlib.Path(".") / ".env"))
    dotenv.load_dotenv(dotenv_path=(pathlib.Path("../") / ".env"))
