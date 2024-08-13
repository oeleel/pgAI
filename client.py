from dotenv import load_dotenv
load_dotenv()

import os

from supabase import create_client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

supabase = create_client(url, key)

data = supabase.table("players_test").select("first_name, last_name").execute()
print(data)