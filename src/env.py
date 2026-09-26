import dotenv
from pathlib import Path
from dotenv import load_dotenv
from dataclasses import dataclass, fields

@dataclass
class Credentials:
    riot_api_key: str
    korean_game_data_url: str
    korean_player_data_url: str

class env:
    def load_env(self):
        ROOT = Path(__file__).resolve().parent.parent
        DOTENV_PATH = ROOT / '.env'
        load_dotenv(DOTENV_PATH)

        credentials = Credentials(
            riot_api_key = dotenv.get_key(DOTENV_PATH, 'RIOT_API_KEY'),
            korean_game_data_url = dotenv.get_key(DOTENV_PATH, 'KOREAN_GAME_DATA_URL'),
            korean_player_data_url = dotenv.get_key(DOTENV_PATH, 'KOREAN_PLAYER_DATA_URL') 
        )

        for field in fields(credentials):
            if not getattr(credentials, field.name):
                raise ValueError(f"{field.name} is not set in the .env file.")

        print("Environment variables loaded successfully.")
        return credentials