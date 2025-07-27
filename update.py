import sqlite3

def add_column_if_not_exists(cursor, table, column, column_type):
    cursor.execute(f"PRAGMA table_info({table})")
    columns = [info[1] for info in cursor.fetchall()]
    if column not in columns:
        cursor.execute(f"ALTER TABLE {table} ADD COLUMN {column} {column_type}")

conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# Safely add new columns to personas
add_column_if_not_exists(cursor, 'personas', 'journal_count', 'INTEGER DEFAULT 0')
add_column_if_not_exists(cursor, 'personas', 'goals_completed', 'INTEGER DEFAULT 0')
add_column_if_not_exists(cursor, 'personas', 'last_updated', 'TEXT DEFAULT CURRENT_DATE')

conn.commit()
conn.close()
print("✅ Columns added successfully (if not already present).")
