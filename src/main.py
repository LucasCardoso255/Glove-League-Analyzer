from env import env
from database.supabase import dbConn
from controller.riotController import RiotController
from models.player import LeagueLeaderboards

# credentials = env().load_env()
# db = dbConn(credentials.supabase_url, credentials.supabase_key)

test = RiotController()
leaderboard: LeagueLeaderboards = test.get_leaderboard_kr()
print(leaderboard.entries[0].puuid)

# top1_puuid = map_leaderboard_data(fetch_korean_leaderboard_data())[0].puuid