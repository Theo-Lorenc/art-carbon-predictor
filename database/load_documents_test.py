import sqlite3

conn = sqlite3.connect("database/carbon.db")

cursor = conn.cursor()

cursor.execute("""
INSERT INTO project_documents
(
    project_id,
    document_name,
    document_title,
    document_type,
    document_category,
    upload_date,
    download_url
)
VALUES (?, ?, ?, ?, ?, ?, ?)
""",
(
    "ART0132",
    "TREES-Concept_Central_African_Republic_2026.pdf",
    "TREES-Concept Central African Republic 2026",
    "TREES Concept",
    "TREES Concept Docs",
    "2026-07-15",
    "/download/example"
))

conn.commit()

conn.close()

print("Document inserted")