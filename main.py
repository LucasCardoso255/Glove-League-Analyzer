import requests
from env import env

env = env().load_env()

def fetch_korean_game_data():
    headers = {
        "X-Riot-Token": f'{env["riot_api_key"]}'
    }
    res = requests.get(env["korean_game_data_url"], headers=headers)

    if res.status_code == 200:
        return res.json()
    else:
        raise Exception(f"Failed to fetch data: {res.status_code} - {res.text}")
    
