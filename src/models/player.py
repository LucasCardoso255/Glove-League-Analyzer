from pydantic import BaseModel

class PlayerLeaderboards(BaseModel):
    puuid: str
    leaguePoints: int
    rank: str
    wins: int
    losses: int
    veteran: bool
    inactive: bool
    freshBlood: bool
    hotStreak: bool

class LeagueLeaderboards(BaseModel):
    tier: str
    queue: str
    entries: list[PlayerLeaderboards]