import sqlite3
import pandas as pd

conn = sqlite3.connect("database/carbon.db")

query = """
SELECT
    project_id,
    COUNT(*) AS rows,
    COUNT(DISTINCT document_name) AS unique_docs

FROM project_documents

GROUP BY project_id

ORDER BY rows DESC
"""

df = pd.read_sql(query, conn)

print(df)

conn.close()