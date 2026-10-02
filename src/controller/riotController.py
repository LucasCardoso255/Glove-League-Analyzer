from env import env
from service.riotService import RiotService

class riotController:
    credentials = env().load_env()
    riotservice = RiotService(credentials)

    async def get_player_kr(self, player_uuid):
        try:
            res = self.get_player_data(player_uuid)
            if res.status_code == 200:
                return self.map_player_data(res) # adicionar self
            else:
                raise Exception(f"Failed to fetch data: {res.status_code} - {res.text}")
        except:
            print("An Error has ocurred.")

    async def get_leaderboard_kr(self):
        try:
            res = self.riotservice.get_leaderboard_data()
            if res.status_code == 200:
                return self.riotservice.map_leaderboard_data(res)
            else:
                raise Exception(f"Failed to fetch data: {res.status_code} - {res.text}")
        except:
            print("An Error has ocurred.")