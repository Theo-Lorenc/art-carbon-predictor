import sqlite3
import pandas as pd

conn = sqlite3.connect("database/carbon.db")

query = """
SELECT
    document_title,
    download_url

FROM project_documents

WHERE
    project_id = 'ART0126'
    AND document_title LIKE '%verification%'
"""

df = pd.read_sql(query, conn)

print(df.to_string())

conn.close()