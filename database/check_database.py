import sqlite3

conn = sqlite3.connect("database/carbon.db")
cursor = conn.cursor()

print("\n=== CHECK 1: Document Counts ===")

cursor.execute("""
SELECT
    project_id,
    COUNT(*) AS rows,
    COUNT(DISTINCT document_name) AS unique_docs
FROM project_documents
GROUP BY project_id
ORDER BY rows DESC
""")

for row in cursor.fetchall():
    print(row)

print("\n=== CHECK 2: Project Details Count ===")

cursor.execute("""
SELECT COUNT(*)
FROM project_details
""")

print(cursor.fetchone())

print("\n=== CHECK 3: Actual Duplicate Documents ===")

cursor.execute("""
SELECT
    project_id,
    document_name,
    COUNT(*)
FROM project_documents
GROUP BY project_id, document_name
HAVING COUNT(*) > 1
""")

rows = cursor.fetchall()

print(f"Duplicates found: {len(rows)}")

for row in rows[:20]:
    print(row)

conn.close()