import dotenv
from pathlib import Path
from dotenv import load_dotenv

class env:
    def load_env(self):
        ROOT = Path(__file__).resolve().parent
        DOTENV_PATH = ROOT / '.env'
        load_dotenv(DOTENV_PATH)

        env = {
            "riot_api_key": dotenv.get_key(DOTENV_PATH, 'RIOT_API_KEY'),
            "korean_game_data_url": dotenv.get_key(DOTENV_PATH, 'KOREAN_GAME_DATA_URL')

        }
        if not dotenv.get_key(DOTENV_PATH, 'RIOT_API_KEY'):
            raise ValueError("RIOT_API_KEY is not set in the .env file.")

        if not dotenv.get_key(DOTENV_PATH, 'KOREAN_GAME_DATA_URL'):
            raise ValueError("KOREAN_GAME_DATA_URL is not set in the .env file.")

        print("Environment variables loaded successfully.")
        return env