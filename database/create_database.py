import sqlite3

conn = sqlite3.connect("database/carbon.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS projects (
    project_id TEXT PRIMARY KEY,
    project_key TEXT,
    project_name TEXT,
    country TEXT,
    project_type TEXT,
    methodology TEXT,
    developer TEXT,
    crediting_program TEXT,
    jurisdiction TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS project_snapshots (
    snapshot_id INTEGER PRIMARY KEY AUTOINCREMENT,
    snapshot_date TEXT,
    project_id TEXT,
    project_status TEXT,
    issued_credits INTEGER,
    last_status_changed TEXT
)
""")

conn.commit()

print("Database structure created")

conn.close()