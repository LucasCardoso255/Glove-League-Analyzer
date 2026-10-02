from env import env
from database.supabase import dbConn

credentials = env().load_env()
db = dbConn(credentials.supabase_url, credentials.supabase_key)

# top1_puuid = map_leaderboard_data(fetch_korean_leaderboard_data())[0].puuid