# database/insert_snapshot.py

import sqlite3

conn = sqlite3.connect("database/carbon.db")

cursor = conn.cursor()

cursor.execute("""
INSERT INTO project_snapshots
(
    snapshot_date,
    project_id,
    project_status,
    issued_credits,
    last_status_changed
)
VALUES
(
    '2026-09-02',
    'ART0131',
    'ACTIVE',
    1669630,
    '2026-07-13'
)
""")

conn.commit()

print("Record inserted")

conn.close()