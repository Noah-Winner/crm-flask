import sqlite3

def verbindung():
    conn = sqlite3.connect("crm.db")
    conn.row_factory = sqlite3.Row
    return conn

def tabelle_erstellen():
    conn = verbindung()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS kunden (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            telefon TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()