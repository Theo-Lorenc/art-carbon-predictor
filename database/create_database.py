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

cursor.execute("""
CREATE TABLE IF NOT EXISTS project_documents (

    document_id INTEGER PRIMARY KEY AUTOINCREMENT,

    project_id TEXT,

    document_name TEXT,
    document_title TEXT,

    document_type TEXT,
    document_category TEXT,

    upload_date TEXT,

    download_url TEXT,

    UNIQUE(
        project_id,
        document_name
    )
)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS project_details (

    project_id TEXT PRIMARY KEY,

    project_listing_status TEXT,

    project_creation_date TEXT,

    project_start_date TEXT,

    current_crediting_period_start TEXT,

    current_crediting_period_end TEXT,

    project_holdings_total_quantity REAL,

    updated_at TEXT

)
""")

conn.commit()

print("Database structure created")

conn.close()