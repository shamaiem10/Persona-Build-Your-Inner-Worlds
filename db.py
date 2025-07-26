# db.py

import sqlite3
from datetime import datetime

DB_NAME = 'persona.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS personas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        mood TEXT,
        quote TEXT,
        goals TEXT,
        thought TEXT,
        theme TEXT,
        last_active TEXT
    )''')
    conn.commit()
    conn.close()

def add_persona(name, mood, quote, goals, thought, theme):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    last_active = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute('''INSERT INTO personas (name, mood, quote, goals, thought, theme, last_active)
                 VALUES (?, ?, ?, ?, ?, ?, ?)''',
              (name, mood, quote, goals, thought, theme, last_active))
    conn.commit()
    conn.close()

def get_all_personas():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM personas")
    data = c.fetchall()
    conn.close()
    return data

def get_persona_by_id(id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM personas WHERE id = ?", (id,))
    data = c.fetchone()
    conn.close()
    return data
