import requests
import json
from env import env
from models.player import PlayerLeaderboards, LeagueLeaderboards

credentials = env().load_env()
headers = {"X-Riot-Token": f'{credentials.riot_api_key}'}

def fetch_korean_game_data():    # controller?
    res = requests.get(credentials.korean_game_data_url, headers=headers)

    if res.status_code == 200:
        return res.json()
    else:
        raise Exception(f"Failed to fetch data: {res.status_code} - {res.text}")

def map_leaderboards(api_response) -> list[PlayerLeaderboards]: # service?
    league_leaderboards = LeagueLeaderboards.model_validate(api_response)
    return league_leaderboards.entries

def fetch_korean_player_data(puuid): # controller?
    res = requests.get(credentials.korean_player_data_url+puuid, headers)

top1_puuid = map_leaderboards(fetch_korean_game_data())[0].puuid