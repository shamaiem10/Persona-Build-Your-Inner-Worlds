import sqlite3

conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# Helper: Add column if it doesn’t already exist
def add_column_if_not_exists(table, column_name, column_type_with_default):
    try:
        cursor.execute(f"ALTER TABLE {table} ADD COLUMN {column_name} {column_type_with_default}")
        print(f"✅ Added column '{column_name}' to '{table}' table.")
    except sqlite3.OperationalError as e:
        if f'duplicate column name: {column_name}' in str(e).lower():
            print(f"⚠️ Column '{column_name}' already exists in '{table}', skipping.")
        else:
            raise

# Add new columns to the personas table
add_column_if_not_exists('personas', 'journal_count', 'INTEGER DEFAULT 0')
add_column_if_not_exists('personas', 'goals_completed', 'INTEGER DEFAULT 0')
add_column_if_not_exists('personas', 'last_updated', 'TEXT')  # Fixed here

conn.commit()
conn.close()
print("🎉 Personas table updated successfully.")
