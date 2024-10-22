import sqlite3
from datetime import datetime

DB_NAME = "journal.db"

def connect_db():
    return sqlite3.connect(DB_NAME)

def create_table():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS journal_entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT,
                date TEXT,
                mood TEXT,
                content TEXT,
                tags TEXT
            )
        ''')
        conn.commit()

def add_entry(user_id, mood, content, tags):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO journal_entries (user_id, date, mood, content, tags)
            VALUES (?, ?, ?, ?, ?)
        ''', (user_id, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), mood, content, tags))
        conn.commit()

def search_entries(user_id, search_term=None, date=None):
    with connect_db() as conn:
        cursor = conn.cursor()

        if search_term:
            query = '''
                SELECT * FROM journal_entries 
                WHERE user_id = ? AND (content LIKE ? OR tags LIKE ?)
            '''
            cursor.execute(query, (user_id, f'%{search_term}%', f'%{search_term}%'))
        elif date:
            query = '''
                SELECT * FROM journal_entries 
                WHERE user_id = ? AND date(date) = ?
            '''
            cursor.execute(query, (user_id, date.strftime('%Y-%m-%d')))
        else:
            return []

        return cursor.fetchall()

# Create the journal table at the start
create_table()
