# database.py
import sqlite3
import bcrypt

def init_db():
    conn = sqlite3.connect("passwords.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS history(username TEXT, hash BLOB)")
    conn.commit()
    conn.close()

def is_reused(username, password):
    conn = sqlite3.connect("passwords.db")
    cur = conn.cursor()
    cur.execute("SELECT hash FROM history WHERE username=?", (username,))
    rows = cur.fetchall()
    conn.close()

    for (h,) in rows:
        if bcrypt.checkpw(password.encode(), h):
            return True
    return False

def save_password(username, password):
    conn = sqlite3.connect("passwords.db")
    cur = conn.cursor()
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    cur.execute("INSERT INTO history VALUES (?,?)", (username, hashed))
    conn.commit()
    conn.close()