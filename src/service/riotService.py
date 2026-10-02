import requests
from models.player import PlayerLeaderboards, LeagueLeaderboards, Player
from env import Credentials

class RiotService:
    def __init__(self, credentials: Credentials):
        self.credentials = credentials 
        self.headers = { "X-Riot-Token": credentials.riot_api_key }

    def map_leaderboard_data(data_to_map) -> list[PlayerLeaderboards]:
        league_leaderboards = LeagueLeaderboards.model_validate(data_to_map)
        return league_leaderboards

    def get_leaderboard_data(self):
        res = requests.get(self.credentials.korean_game_data_url, self.headers)
        return res

    def get_player_data(self, puuid):
        res = requests.get(self.credentials.korean_player_data_url+puuid, self.headers)
        return res

    def map_player_data(data_to_map) -> algumaporra[daAPIdaRiot]:
        player = Player.model_validate(data_to_map)
        return player