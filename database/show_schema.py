import sqlite3

conn = sqlite3.connect("database/carbon.db")
cursor = conn.cursor()

cursor.execute("""
SELECT sql
FROM sqlite_master
WHERE name='project_documents'
""")

print(cursor.fetchone()[0])

conn.close()