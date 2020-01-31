import sqlite3 as sqlite

DB_NAME = "Shop.db"


conn = sqlite.connect(DB_NAME)

conn.cursor().execute('''
CREATE TABLE IF NOT EXISTS user
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT,
        email TEXT,
        address TEXT,
        phone_number TEXT
    )
''')
conn.commit()

conn.cursor().execute('''
CREATE TABLE IF NOT EXISTS ads
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        title TEXT NOT NULL UNIQUE,
        description TEXT,
        price DOUBLE,
        date TEXT,
        isActive BOOL,
        buyer TEXT
    )
''')
conn.commit()

class SQLite(object):
    
    def __enter__(self):
        self.conn = sqlite.connect(DB_NAME)
        return self.conn.cursor()

    def __exit__(self, type, value, traceback):
        self.conn.commit()