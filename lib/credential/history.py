import os
import shutil
import sqlite3
from datetime import datetime, timedelta

LOCAL = os.getenv("LOCALAPPDATA")
PATHS = {
    'Chrome': os.path.join(LOCAL, 'Google', 'Chrome', 'User Data'),
    'Edge': os.path.join(LOCAL, 'Microsoft', 'Edge', 'User Data'),
}

def historys():
    res = []

    for browser, path in PATHS.items():
        if not os.path.exists(path):
            continue

        for profile in os.listdir(path):
            if profile != "Default" and not profile.startswith("Profile"): 
                continue

            db_path = os.path.join(path, profile, "History")
            if not os.path.exists(db_path):
                continue

            tmp_db = os.path.join(os.getenv("TEMP"), "tmp_history.db")
            shutil.copy2(db_path, tmp_db)
            conn = sqlite3.connect(tmp_db)
            cur = conn.cursor()
            cur.execute("SELECT url, title, last_visit_time FROM urls ORDER BY last_visit_time DESC")

            for url, title, last_visit in cur.fetchall():
                t = datetime(1601, 1, 1) + timedelta(microseconds=last_visit)
                res.append({
                    "browser": browser,
                    "url": url,
                    "title": title,
                    "visit": t.strftime("%Y-%m-%d %H:%M:%S")
                })

            cur.close()
            conn.close()
            os.remove(tmp_db)

    return res