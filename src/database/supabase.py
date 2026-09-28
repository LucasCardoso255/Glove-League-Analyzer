from supabase import create_client, Client

def dbConn(DB_URL: str, DB_KEY: str) -> Client:
    supabase: Client = create_client(DB_URL, DB_KEY)
    return supabase
