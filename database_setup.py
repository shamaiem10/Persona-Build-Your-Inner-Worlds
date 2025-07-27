import sqlite3

conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# Table for storing different personas
cursor.execute('''
CREATE TABLE IF NOT EXISTS personas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    mood TEXT,
    quote TEXT,
    theme TEXT,
    last_active TEXT
)
''')

# Table for storing chat messages between personas
cursor.execute('''
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    persona_id INTEGER,
    message TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (persona_id) REFERENCES personas(id)
)
''')

# Table for storing goals for each persona
cursor.execute('''
CREATE TABLE IF NOT EXISTS goals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    persona_id INTEGER,
    task TEXT,
    is_done BOOLEAN DEFAULT 0,
    FOREIGN KEY (persona_id) REFERENCES personas(id)
)
''')

# Table for storing journal entries per persona
cursor.execute('''
CREATE TABLE IF NOT EXISTS journals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    persona_id INTEGER,
    entry TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (persona_id) REFERENCES personas(id)
)
''')



conn.commit()
conn.close()
print("Database and tables created successfully.")
