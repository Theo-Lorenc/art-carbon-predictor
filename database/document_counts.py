import sqlite3
import pandas as pd

conn = sqlite3.connect("database/carbon.db")

query = """
SELECT
    project_id,
    COUNT(*) AS document_count

FROM project_documents

GROUP BY project_id

ORDER BY document_count DESC
"""

df = pd.read_sql(query, conn)

print(df)

conn.close()