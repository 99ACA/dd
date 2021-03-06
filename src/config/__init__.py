
from os import path

from dotenv import load_dotenv

_env_path = f"{path.dirname(__file__)}/../../.env"

load_dotenv(dotenv_path=_env_path)
