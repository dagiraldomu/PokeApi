import os
from dotenv import load_dotenv
from threading import Lock

def load_env():
    dotenv_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
    if os.path.isfile(dotenv_path):
        load_dotenv(dotenv_path)


class Settings:
    _instance = None
    _lock: Lock = Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                load_env()
                cls._instance = super(Settings, cls).__new__(cls)
                # Singleton
                cls._instance.poke_api_berry_url = os.environ.get('POKEAPI_BERRY_URL')
                cls._instance.cache_expire_time = int(os.environ.get('CACHE_EXPIRE_TIME', 60))
        return cls._instance


# Usage
settings = Settings()
