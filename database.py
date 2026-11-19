import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "database.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        skill TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS requests(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sender TEXT,
        receiver TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS chats(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sender TEXT,
        receiver TEXT,
        message TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS codes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sender TEXT,
        receiver TEXT,
        code TEXT,
        error TEXT,
        output TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS modules(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name TEXT,
        title TEXT,
        description TEXT
    )
    ''')

    conn.commit()
    conn.close()

    return DB_PATH


if __name__ == "__main__":
    init_db()
    print("Database Created Successfully")