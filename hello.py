from supabase import create_client, Client
from datetime import datetime
import os

SUPABASE_URL = "https://bhkhyhhnpvwsxjzvxxet.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJoa2h5aGhucHZ3c3hqenZ4eGV0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTExNzU5OTcsImV4cCI6MjA2Njc1MTk5N30.2AW1-y-cILgVVdpCTbcezgUD04JsGWPRZG-1ZLhPGK0"  # Replace with your actual anon key

def log_run_time():
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    data = {"run_time": datetime.now().isoformat()}
    supabase.table("runs").insert(data).execute()

def main():
    print("Hello from GitHub Actions cron job!")
    print("last time updated on :", datetime.now().isoformat())
    log_run_time()

if __name__ == "__main__":
    main()