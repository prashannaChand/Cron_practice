#dummy testing for cron 
import os
import sys
import sqlite3
from datetime import datetime

def log_run_time():
    conn = sqlite3.connect('cron_runs.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS runs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            run_time TEXT NOT NULL
        )
    ''')
    c.execute('INSERT INTO runs (run_time) VALUES (?)', (datetime.now().isoformat(),))
    conn.commit()
    conn.close()

def main():
    print("Hello from GitHub Actions cron job!")
    print("last time updated on :", os.path.getmtime(__file__))
    log_run_time()

if __name__ == "__main__":
    main()
    sys.exit(0)