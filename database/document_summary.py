import sqlite3
import pandas as pd

conn = sqlite3.connect("database/carbon.db")

df = pd.read_sql(
    """
    SELECT
        document_type,
        COUNT(*) as count
    FROM project_documents
    GROUP BY document_type
    ORDER BY count DESC
    """,
    conn
)

print(df)

print()
print("Unique document types:",
      len(df))

conn.close()